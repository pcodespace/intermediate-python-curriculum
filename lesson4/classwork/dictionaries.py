# A dictionary maps keys to values.
person = {
    "name": "Parjanya", 
    "age": 10,
    "city": "Bothell"
}

print(person)
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Update a value
person["age"] = person["age"] + 1
print("New Age:", person["age"])

# Add a new key
person["favorite_food"] = "pizza"
print(person)