class Parent:
    def show(self):
        print("This is the Parent class.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
obj1.show()
obj2.show()
