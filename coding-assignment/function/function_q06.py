'''6. How to define a function with keyword arguments?
Question: How can you define a function greet that accepts name and age as keyword arguments?'''

# Defining a function with keyword arguments
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

# Calling the function with keyword arguments
greet(name="Alice", age=30)