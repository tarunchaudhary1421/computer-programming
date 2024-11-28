'''8. How to define a function that raises an exception?
Question: How can you define a function divide that raises an exception if attempting to divide by zero?'''

# Defining a function that raises an exception
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Calling the function with error handling
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)