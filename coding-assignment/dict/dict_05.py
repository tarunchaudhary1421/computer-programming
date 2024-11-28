'''5. How to remove a key-value pair from a dictionary?
Question: How can you remove the key "age" from the dictionary?'''


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Removing a key-value pair from the dictionary
del person["age"]
print(person)
