'''9. How to merge two dictionaries?
Question: How can you merge the dictionary person with another dictionary address?'''


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Merging two dictionaries
address = {
    "street": "123 Main St",
    "zip": "10001"
}

person.update(address)
print(person)
