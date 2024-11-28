'''4. How to check if a key exists in a dictionary?
Question: How can you check if the key "city" exists in the dictionary?'''


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Checking if a key exists
if "city" in person:
    print("City exists in the dictionary.")
else:
    print("City does not exist.")
