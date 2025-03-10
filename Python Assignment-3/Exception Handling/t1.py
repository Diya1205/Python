def fun(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

fun(10, 2)
fun(10, 0)
fun(10, 'a')
