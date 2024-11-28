'''10. How to use a function as an argument to another function?
Question: How can you pass a function square as an argument to another function apply_function?'''

# Defining a function to be passed as an argument
def square(x):
    return x * x

# Defining a function that accepts another function as an argument
def apply_function(func, value):
    return func(value)

# Calling the function
result = apply_function(square, 5)
print(result)