# Start with an empty list
numbers = []

# Add numbers to the list using append
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# Build a list of squares
squares = []
for i in range(1, 101):
    squares.append(i * i)
print(squares)

# Build a list with only even numbers
evens = []
for i in range(0, 101):
    if i % 2 == 0:
        evens.append(i)
print(evens)