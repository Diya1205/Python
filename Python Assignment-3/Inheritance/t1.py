class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    pass  # Inherits the show() method from Parent

obj = Child()
obj.show()
