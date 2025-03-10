class A:
    def showA(self):
        print("This is class A.")

class B(A):  
    def showB(self):
        print("This is class B.")

class C(A): 
    def showC(self):
        print("This is class C.")

class D(B, C):  
    def showD(self):
        print("This is class D.")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
