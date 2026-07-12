# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
print("-----------------------------Problem 1--------------------------------------------------")
sentence = input("Give me a sentence.")
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print(freq)

# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
capitals = {
    "Washington": "Olympia",
    "Oregon": "Salem",
    "Texas": "Austin"
}
state = input("Enter a state.")
if state in capitals:
    print(capitals[state])
else:
    print("No data of the state you entered found.")

# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
word = input("Give me a word.")
letter_freq = {}
for letter in word:
    if letter in letter_freq:
        letter_freq[letter] = letter_freq[letter] + 1
    else:
        letter_freq[letter] = 1

max_letter = max(letter_freq, key=letter_freq.get)
print(max_letter)

# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
inventory = {
    "cookie": 7,
    "cupcake": 8,
    "doughnut": 12,
    "pie": 9
}
buy = input("Tell me which item you want to buy at the little dessert store.")
quantity = int(input("How many of that dessert would you like to buy? "))

if buy in inventory and inventory[buy] >= quantity:
    inventory[buy] -= quantity
    print("Your purchase is successful!")
    print("New inventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")
else:
    print("Not enough of that dessert you want to buy is available.")

# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

freq1 = {}
for letter in word1:
    if letter in freq1:
        freq1[letter] = freq1[letter] + 1
    else:
        freq1[letter] = 1

freq2 = {}
for letter in word2:
    if letter in freq2:
        freq2[letter] = freq2[letter] + 1
    else:
        freq2[letter] = 1

if freq1 == freq2:
    print("Your words are anagrams.")
else:
    print("Your words are not anagrams.")