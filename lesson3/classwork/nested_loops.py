# A nested loop is a loop inside another loop
for i in range(3):
    for j in range(4):
        print("i:", i, "j:", j)

# You can use range(start, stop) with nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print("i:", i, "j:", j)

# Build rows of stars using nested loops
for row in range(3):
    line = ""
    for col in range(5):
        line = line + "*"
    print(line)