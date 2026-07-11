# Problem 1
# Create a dictionary called student with these keys:
# "name" -> your name
# "grade" -> your grade level
# Print the dictionary and then print only the name.
print("-----------------------------------Problem 1---------------------------------------------------------")
student = {
    "name": "Parjanya",
    "grade": 5
}
print(student)
print("Name:", student["name"])

# Problem 2
# Create a dictionary called prices with:
# "apple" -> 2
# "banana" -> 1
# "orange" -> 3
# Ask the user for a fruit name and print its price.
# If the fruit is not in the dictionary, print "Not found".
print("-----------------------------------Problem 2---------------------------------------------------------")
prices = {
    "apple": 2,
    "banana": 1,
    "orange": 3
}
fruit = input("Choose your fruit:")
if fruit in prices:
    print("Price:", prices[fruit])
else:
    print("The fruit you are looking for is not found in the dictionary.")
# Problem 3
# Ask the user for a word.
# Use a dictionary to count how many times each letter appears.
# Print the dictionary.
print("-----------------------------------Problem 3---------------------------------------------------------")
word = input("Give me a word:")
freq = {}
for letter in word:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1
print(freq)

# Problem 4
# Create a dictionary called phonebook with 3 names and phone numbers.
# Ask the user for a name and print the phone number if it exists.
# Otherwise print "Unknown contact".
print("-----------------------------------Problem 4---------------------------------------------------------")
phonebook = {
    "Athan": "563-619-7132",
    "Parjanya": "603-102-2173",
    "Aaron": "581-670-1639"
}
name = input("Enter a name:")
if name in phonebook:
    print("Phone number:", phonebook[name])
else:
    print("Unknown contact.")

# Problem 5
# Create a dictionary called scores with 3 students and their test scores.
# Print the name of the student with the highest score.
print("-----------------------------------Problem 5---------------------------------------------------------")
scores = {
    "Lucas": 108,
    "Jackson": 102,
    "Kyra": 91
}
best_name = ""
best_score = -1
for name in scores:
    if scores[name] > best_score:
        best_score = scores[name]
        best_name = name
print("The student with the highest score is:", best_name)

# Problem 6
# Create a dictionary that stores student names and scores
# Keep adding or updating scores until the user enters "done".
# Print the lowest score of the students.
print("-----------------------------------Problem 6---------------------------------------------------------")
scores = {}
flag = True
while flag == True:
    name = input("Enter a student name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    score = int(input("Enter the student's score: "))
    scores[name] = score
lowest_score = 101
for name in scores:
    if scores[name] < lowest_score:
        lowest_score = scores[name]
print("The lowest score is:", lowest_score)