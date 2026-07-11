prices = {
    "apple": 1,
    "banana": 2,
    "orange": 3
}

# Check if a key is in the dictionary before using it
fruit = "apple"
if fruit in prices:
    print("Price:", prices[fruit])
else:
    print("Not found.")