# Global variable
x = 10  

class A:
    def fun(self):
        # Local variable
        y = 20  
        print("Global variable:", x)
        print("Local variable:", y)

# Create an object of the class
obj = A()
obj.fun()
