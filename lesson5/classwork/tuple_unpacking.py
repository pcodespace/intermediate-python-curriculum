# Unpacking a tuple
point = (8, 2)
x, y = point
print("x is:", x)
print("y is:", y)

# Swapping values with tuples
a = 5
b = 9
a, b = b, a
print(a, b)

# You can return multiple values from a function as a tuple.
def min_and_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest

nums = [4, 12, 7, 1, 9]
min, max = min_and_max(nums)
print("Min:", min)
print("Max:", max)