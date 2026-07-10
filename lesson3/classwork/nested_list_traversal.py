# A 2D list is a list inside another list
scores = [
    [90, 80, 70],
    [100, 95, 85],
    [60, 75, 88]
]

print(scores)
print(scores[0]) # first row
print(scores[0][1]) # first row, second item

# Loop through every item in a nested list
for row in range(len(scores)):
    for col in range(len(scores[row])):
        print(scores[row][col])