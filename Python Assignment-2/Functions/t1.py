x = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
y = float(input("Enter second number: "))

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/' and y != 0:
    print(x / y)
else:
    print("Invalid input")
