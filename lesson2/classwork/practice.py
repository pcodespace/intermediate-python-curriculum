# Problem 1
# Ask the user for a word.
# Print the first 3 letters, and then print the last 3 letters.
word = (input("Enter a word: "))
print("First 3 letters:", word[:3])
print("Last 3 letters:", word[-3:])

# Problem 2
# Ask the user for a sentence.
# Print it in all caps, then print it in all lowercase.
sentence = input("Enter a sentence: ")
print("All caps:", sentence.upper())
print("All lowercase:", sentence.lower())

# Problem 3
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).
word = input("Enter a word: ")
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print("Number of vowels:", count)

# Problem 4
# Ask the user for a phrase.
# Build a new string that removes all spaces.
phrase = input("Enter a phrase: ")
new_string = phrase.replace(" ", "")
print("String without spaces:", new_string)

# Problem 5
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".
word = input("Enter a word:")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")