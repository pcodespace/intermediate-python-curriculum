# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
print("---------------------------------Problem 1------------------------------------------------")
number = int(input("What is your number?"))
for i in range(0, number+1, 3):
    print("Multiples of 3:", i)

# Problem 2
# Ask the user for a number n.
# Build a list of the squares from 1*1 up to n*n.
# Print the list.
print("---------------------------------Problem 2------------------------------------------------")
num = int(input("Give me a number."))
squares = []
for i in range(0, num + 1):
    squares.append(i * i)
print(squares)


# Problem 3
# Use nested loops to print a triangle of stars with 5 rows.
# The first row has 1 star, the second row has 2 stars, and so on.
print("---------------------------------Problem 3------------------------------------------------")
for row in range(5):
    line = ""
    for col in range(row + 1):
        line = line + "*"
    print(line)


# Problem 4
# Create a 2D list of numbers.
# Count how many numbers are greater than 10.
print("---------------------------------Problem 4------------------------------------------------")
numbers = [
    [11, 5, 9],
    [8, 15, 12],
    [13, 10, 8]
]
count = 0
for row in numbers:
    for num in row:
        if num > 10:
            count += 1
print("The count of numbers greater than 10 is:", count)


# Problem 5
# Create a 2D list of letters.
# Build one string that contains every letter in the 2D list.
# Print the final string.
print("---------------------------------Problem 5------------------------------------------------")
letters = [
    ["w"], ["h"], ["k"],
    ["e"], ["a"], ["l"],
    ["s"], ["u"], ["r"]
]
last_string = ""
for row in letters:
    for letter in row:
        last_string += letter
print("The last string is:", last_string)