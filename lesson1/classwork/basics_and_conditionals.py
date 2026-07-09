print("Hello world!")
x = 5
favorite_food = "pizza"
height = 5.2
likes_python = True
print("x:",x)
print("favorite food:", favorite_food)
print("height:", height)
print("likes python:", likes_python)

num_input = int(input("Give me a number: "))  #input ALWAYS returns a string
print(num_input)
if num_input > 0:
    print("The number is positive.")
elif num_input == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
if num_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
if num_input > 0 and num_input < 100:
    print("The number is between 1 and 99.")
if num_input < 0 or num_input > 100:
    print("The number is not between 1 and 99.")