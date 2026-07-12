# Problem 1
# Create a tuple called colors with 3 colors.
# Print the first color and the last color.
colors = ("voilet", "yellow", "red")
print("First color:", colors[0])
print("Last color:", colors[2])


# Problem 2
# Create a tuple called location with (city, state).
# Unpack it into city and state variables and print them.
location = ("Bothell", "Washington")
city, state = location
print("City:", city)
print("State:", state)


# Problem 3
# Create a list of numbers.
# Sort the list and print it.
numbers = [7, 1, 3, 2, 8]
numbers.sort()
print("Sorted numbers:", numbers)



# Problem 4
# Create a list of tuples called points with 3 points.
# Sort the list and print it.
points = [(3, 5), (1, 9), (1,2)]
points.sort()
print("Sorted points:", points)



# Problem 5
# Create a list of words.
# Sort the words by length and print the list.
words = ["goldfish", "turtle", "whale", "octopus"]
words.sort(key=len)
print("Sorted by length:", words)

# Problem 6
# Create a list of tuples called students with (name, score).
# Sort the list by score and print it with functions.
students = [("Arjun", 96), ("Melia", 87), ("Landon", 85)]
def get_score(student):
    return student[1]

students.sort(key=get_score)
print("Sorted by score:", students)