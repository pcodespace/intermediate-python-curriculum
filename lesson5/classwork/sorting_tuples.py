points = [(3, 5), (1, 9), (1,2), (4, 0)]
print("Original:", points)

# Tuples sort by the first value, then the second value, and so on.
points.sort()
print("Sorted:", points)

students = [("Arjun", 99), ("Melia", 95), ("Landon", 97)]

# Loop through a list of tuples
for name, score in students:
    print(name, score)