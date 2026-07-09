name = "Parjanya"
result = ""
for Madakasira in name:
    result = result + Madakasira +"-"
print(result)

letters = ["p", "y", "t", "h", "o", "n"]
built = "".join(letters)
print(built)

word = "computer"
new_word = ""
for i in range(len(word)):
    if i % 2 == 0:
        new_word = new_word + word[i]
print(new_word)