
# Business logic using OOP, encapsulation, inheritance
class Product:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def get_total(self):
        return self.qty * self.price

class Category:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def get_total(self):
        return sum([item.get_total() for item in self.items])

    def get_items(self):
        return self.items

class Bill:
    def __init__(self, bill_no, customer_name, phone):
        self.bill_no = bill_no
        self.customer_name = customer_name
        self.phone = phone
        self.__total = 0  # Private using encapsulation

    def set_total(self, total):
        self.__total = total

    def get_total(self):
        return self.__total
