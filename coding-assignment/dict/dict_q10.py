'''10. How to iterate over the keys and values of a dictionary?
Question: How can you loop through the dictionary and print each key-value pair?'''


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Iterating over keys and values in the dictionary
for key, value in person.items():
    print(key, ":", value)
