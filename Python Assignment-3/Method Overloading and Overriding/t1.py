# Simulating method overloading using default arguments
class Calculator:
    def add(self, a=0, b=0, c=0):
        print("Sum:", a + b + c)

c = Calculator()
c.add(10, 20)        # Two arguments
c.add(5, 15, 25)     # Three arguments
c.add()              # No arguments
