words = ["dog", "cat", "elephant", "bird"]
print("Original:", words)

# Sort by word instead of alphabetical order
words.sort(key = len) # Sort the list by the length of each word
print("Sorted by length:", words)

students = [("Arjun", 96), ("Melia", 87), ("Landon", 85)]

# A key function tells Python what value to sort by.
def get_score(student):
    return student[1]

students.sort(key=get_score)
print("Sorted by score:", students)

students.sort(key=get_score, reverse=True)
print("Sorted by score backwards:", students)