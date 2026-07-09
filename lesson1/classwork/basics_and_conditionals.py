print("Hello world!")

x = 5
favorite_food = "pizza"
height = 5.2
likes_python = True
print("x:",x)
print("favorite food:", favorite_food)
print("height:", height)
print("likes python:", likes_python)
num = input("Enter a number:")
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
if num > 0 and num < 100:
    print("The number is between 1 and 99.")
if num < 0 or num > 100:
    print("The number is not between 1 and 99.")