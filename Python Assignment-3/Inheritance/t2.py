class Grandparent:
    def show1(self):
        print("This is the Grandparent class.")

class Parent(Grandparent):
    def show2(self):
        print("This is the Parent class.")

class Child(Parent):
    def show3(self):
        print("This is the Child class.")

obj = Child()
obj.show1()
obj.show2()
obj.show3()
