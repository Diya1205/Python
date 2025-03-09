# Lambda function to find sum and product
operations = lambda x, y: (x + y, x * y)

sum_result, product_result = operations(3, 5)
print("Sum:", sum_result)
print("Product:", product_result)
