# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
scores = (83, 100, 78, 92)
average = sum(scores) / len(scores)
print("Average score:", average)


# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
students = [("Ava", 95), ("Ben", 88), ("Kai", 73)]
def get_score(student):
    return student[1]
highest_student = max(students, key=get_score)
print("Student with highest score:", highest_student[0])

# Problem 3
# Create a list of words.
# Sort it alphabetically, then print it.
# Then sort it by length, then print it.
words = ["deer", "bear", "bison", "duck"]
words.sort()
print("Sorted alphabetically:", words)
words.sort(key=len)
print("Sorted by length:", words)


# Problem 4
# Create a list of tuples where each tuple is (word, length_of_word).
# Sort the list and print it.
words_with_length = [("glass", 5), ("cup", 3), ("bowl", 4), ("bottle", 6)]

def get_length(item):
    return item[1]

words_with_length.sort(key=get_length)
print("Sorted by length:", words_with_length)


# Problem 5
# Create a list of tuples called players.
# Each tuple should have (name, score).
# Sort the players from highest score to lowest score and print the list.
players = [("Arjun", 500), ("Melia", 450), ("Landon", 400)]
players.sort(key=lambda player: player[1], reverse=True)
print("Sorted by score (highest to lowest):", players)