
text = " Hello world "
print("Raw text is:", text)

print("Length:", len(text))

print(text.lower())
print(text.upper())
print(text.title())
print(text.strip())
print(text.strip().upper())

message = "banana bread"
print("Count of a:", message.count("a"))
print("Find 'bread':", message.find("bread"))

print(message.replace("banana", "pumpkin"))

print(message.startswith("ban"))
print(message.endswith("bread"))