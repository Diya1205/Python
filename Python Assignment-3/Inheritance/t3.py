class Parent1:
    def show1(self):
        print("This is Parent1.")

class Parent2:
    def show2(self):
        print("This is Parent2.")

class Child(Parent1, Parent2):
    pass  # Inherits methods from both Parent1 and Parent2

obj = Child()
obj.show1()
obj.show2()
