# Problem 1
# Ask the user for their name and age.
# Print a sentence that uses both variables.
print("---------------------------Problem 1---------------------------------")
name_input = input("What is your name?: ")
age_input = float(input("What is your age?: "))
print("Your name and age:", name_input, age_input)

# Problem 2
# Ask the user for a number.
# Print "Positive" if it is more than 0.
# Print "Zero" if it is equal to 0.
# Otherwise print "Negative".
print("------------------------------Problem 2---------------------------------------------")
num_input = float(input("Give me a number:"))
print(num_input)
if num_input > 0:
    print("Your number is positive.")
elif num_input == 0:
    print("Your number is equal to zero.")
else:
    print("Your number is negative.")

# Problem 3
# Create a list of 5 numbers.
# Print the sum of all numbers in the list.
print("----------------------Problem 3----------------------------------")
numbers = [5, -9, 12, -31, 82]
sum = 0
for i in range(len(numbers)):
    item = numbers[i]
    sum = sum + item
print("Sum:", sum)

# Problem 4
# Create a list of 5 animals.
# Count how many times "cat" appears in the list.
print("----------------------Problem 4--------------------------------------------------")
animals = ["cat", "turle", "lion", "cat", "cat"]
count = 0
for i in range(len(animals)):
    item = animals[i]
    if item == "cat":
        count = count + 1
print("The number of cats in the list is:", count)

# Problem 5
# Create a function called bigger(a, b).
# It should return the bigger number.
# Call it and print the result.
print("--------------------------Problem 5----------------------------------------------")
def bigger_number(a, b):
    if a > b :
        return a
    else:
        return b
print("The bigger number is:", bigger_number(-67, 899))