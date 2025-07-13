
import tkinter as tk
from tkinter import messagebox, scrolledtext
from db import Database
from logic import Product, Category, Bill

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing Software")
        self.root.geometry("1050x600")
        self.root.config(bg="#0A3D62")

        # Fonts and colors
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        fg_color = "white"
        bg_color = "#0A3D62"

        # Database object
        self.db = Database()

        # Top title
        tk.Label(root, text="Billing Software", font=("Arial", 20, "bold"), bg=bg_color, fg="white").pack(fill=tk.X)

        # Customer details frame
        f1 = tk.Frame(root, bd=3, relief=tk.GROOVE, bg=bg_color)
        f1.place(x=0, y=40, relwidth=1, height=60)

        tk.Label(f1, text="Customer Name", bg=bg_color, fg=fg_color, font=label_font).place(x=10, y=10)
        self.name_entry = tk.Entry(f1, font=entry_font, width=20)
        self.name_entry.place(x=140, y=10)

        tk.Label(f1, text="Phone No", bg=bg_color, fg=fg_color, font=label_font).place(x=330, y=10)
        self.phone_entry = tk.Entry(f1, font=entry_font, width=20)
        self.phone_entry.place(x=430, y=10)

        tk.Label(f1, text="Bill No.", bg=bg_color, fg=fg_color, font=label_font).place(x=620, y=10)
        self.bill_entry = tk.Entry(f1, font=entry_font, width=10)
        self.bill_entry.place(x=700, y=10)

        tk.Button(f1, text="Enter", font=label_font, command=self.enter_customer).place(x=850, y=6)

        # Product frames
        self.create_product_frame("Cosmetics", 10, 110, ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"])
        self.create_product_frame("Grocery", 270, 110, ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"])
        self.create_product_frame("Others", 530, 110, ["Maza", "Coke", "Frooti", "Nimkos", "Biscuits"])

        # Bill area
        self.bill_area = scrolledtext.ScrolledText(root, font=("Courier New", 10), width=38, height=22)
        self.bill_area.place(x=780, y=110)
        self.bill_area.insert(tk.END, "Welcome to Ranan's Retail")

        # Control buttons
        tk.Button(root, text="Total", width=15, font=label_font, command=self.calculate_total).place(x=150, y=530)
        tk.Button(root, text="Generate Bill", width=15, font=label_font, command=self.generate_bill).place(x=300, y=530)
        tk.Button(root, text="Clear", width=15, font=label_font, command=self.clear_fields).place(x=450, y=530)
        tk.Button(root, text="Exit", width=15, font=label_font, command=root.quit).place(x=600, y=530)

    def create_product_frame(self, title, x, y, items):
        frame = tk.LabelFrame(self.root, text=title, bg="#0A3D62", fg="white", font=("Arial", 12, "bold"), bd=5)
        frame.place(x=x, y=y, width=250, height=250)
        setattr(self, f"{title.lower()}_entries", {})
        for i, item in enumerate(items):
            tk.Label(frame, text=item, font=("Arial", 10, "bold"), bg="#0A3D62", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(frame, width=10)
            entry.grid(row=i, column=1, padx=10, pady=5)
            getattr(self, f"{title.lower()}_entries")[item] = entry

    def enter_customer(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        bill = self.bill_entry.get()
        if not name or not phone or not bill:
            messagebox.showwarning("Input Error", "Please fill all customer details.")
            return
        self.bill_area.insert(tk.END, f"Bill No.: {bill}\nCustomer Name: {name}\nPhone No.: {phone}\n\n")
        self.customer = Bill(bill, name, phone)

    def calculate_total(self):
        self.cosmetics = Category()
        self.grocery = Category()
        self.others = Category()

        categories = [("cosmetics", 40), ("grocery", 60), ("others", 20)]
        total = 0
        for category_name, price in categories:
            entries = getattr(self, f"{category_name}_entries")
            category_obj = getattr(self, category_name)
            for name, entry in entries.items():
                qty = entry.get()
                if qty.isdigit() and int(qty) > 0:
                    p = Product(name, int(qty), price)
                    category_obj.add_product(p)
                    total += p.get_total()
        self.customer.set_total(total)
        messagebox.showinfo("Total Calculated", f"Total Amount: ₹ {total}")

    def generate_bill(self):
        # Check if total is calculated
        if not hasattr(self, 'cosmetics') or not hasattr(self, 'grocery') or not hasattr(self, 'others'):
            messagebox.showwarning("Action Needed", "Please click 'Total' before generating the bill.")
            return

        total = self.customer.get_total()
        lines = ["Product\tQty\tPrice"]
        for cat in [self.cosmetics, self.grocery, self.others]:
            for item in cat.get_items():
                lines.append(f"{item.name}\t{item.qty}\t{item.get_total()}")
        lines.append(f"\nTotal: ₹ {total}")
        final_bill = "\n".join(lines)

        # Save to file
        with open("bill.txt", "w", encoding="utf-8") as f:
            f.write(final_bill)

        # Insert into database
        self.db.insert_bill(self.customer.bill_no, self.customer.customer_name, self.customer.phone, total, final_bill)

        self.bill_area.insert(tk.END, final_bill)
        messagebox.showinfo("Bill Generated", "Bill saved and displayed successfully.")


    def clear_fields(self):
        for frame in [self.cosmetics_entries, self.grocery_entries, self.others_entries]:
            for entry in frame.values():
                entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.bill_entry.delete(0, tk.END)
        self.bill_area.delete('1.0', tk.END)
        self.bill_area.insert(tk.END, "Welcome to Ranan's Retail\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
