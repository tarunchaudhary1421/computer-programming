'''4. How to define a function with default parameters?
Question: How can you define a function greet that accepts a name with a default value of "Guest"?'''

# Defining a function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet("Bob")
greet()