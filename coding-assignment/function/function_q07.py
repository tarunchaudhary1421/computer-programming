'''7. How to define a recursive function?
Question: How can you define a function factorial that computes the factorial of a number using recursion?'''

# Defining a recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
result = factorial(5)
print(result)