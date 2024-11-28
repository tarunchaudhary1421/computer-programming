'''5. How to define a function with variable number of arguments?
Question: How can you define a function add_all that accepts any number of numbers and returns their sum?'''

# Defining a function with variable arguments
def add_all(*numbers):
    return sum(numbers)

# Calling the function
result = add_all(1, 2, 3, 4)
print(result)