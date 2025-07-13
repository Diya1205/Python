
import pymysql

class Database:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",  # Set your MySQL password
                database="billing_db"
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("Database connection failed:", e)

    def insert_bill(self, bill_no, customer_name, phone, total, bill_text):
        try:
            query = "INSERT INTO bills (bill_no, customer_name, phone, total, bill_text) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (bill_no, customer_name, phone, total, bill_text))
            self.connection.commit()
            return True
        except Exception as e:
            print("Insert Error:", e)
            return False

    def delete_bill(self, bill_no):
        try:
            query = "DELETE FROM bills WHERE bill_no=%s"
            self.cursor.execute(query, (bill_no,))
            self.connection.commit()
            return True
        except Exception as e:
            print("Delete Error:", e)
            return False

    def fetch_bill(self, bill_no):
        try:
            query = "SELECT * FROM bills WHERE bill_no=%s"
            self.cursor.execute(query, (bill_no,))
            return self.cursor.fetchone()
        except Exception as e:
            print("Fetch Error:", e)
            return None

    def close(self):
        self.connection.close()
