word = "pineapple"
print("Word is:", word)

print("First letter:", word[0])
print("Second letter:", word[1])
print("Last letter:", word[-1])
print("Second to last letter:", word[-2])

print(word[0:4])
print(word[4:9])
print(word[:4])
print(word[4:])

print(word[::-1])
# Error: index out of range
# print(word[100])