# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
word = input("Give me a word.")
print("First letter:", word[0])
print("Second letter:", word[1])
print("Second to last letter:", word[-2])
print("Last letter:", word[-1])
print(word[::-1])


# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive).
word2 = input("Give me a word.")
letter = input("Give me a letter.")
word2_lower = word2.lower()
letter_lower = letter.lower()
count = word2_lower.count(letter_lower)
print(count)


# Problem 3
# Ask the user for a first name and a last name.
# Print their initials (first letter of first name + first letter of last name).
first_name = input("Give me your first name.")
last_name = input("Give me your last name.")
initials = first_name[0] + last_name[0]
print("Your initials are:", initials)

# Problem 4
# Ask the user for a sentence.
# Replace all spaces with underscores and print the result.
sentence = input("Give me a sentence.")
result = sentence.replace(" ", "_")
print("Result:", result)

# Problem 5
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).
word = input("Give me a word.")
odd_indexed_letters = word[::2]
print("Letters at odd indexes:", odd_indexed_letters)