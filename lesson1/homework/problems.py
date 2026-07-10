# Problem 1
# Ask the user for two numbers.
# Print their sum, difference, and product.
print("-----------------------------Problem 1--------------------------------------")
num1 = float(input("What is your first number?"))
num2 = float(input("What is your second number?"))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
print("The sum is ", sum, "The difference is", difference, "The product is:", product)


# Problem 2
# Ask the user for a number.
# Print whether the number is even or odd.
print("----------------------------Problem 2------------------------------------")
num = int(input("Enter a number."))
if num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")


# Problem 3
# Create a list of numbers.
# Print the biggest number in the list.
print("----------------------Problem 3---------------------------------------")
numbers = [14, -9, 18, 3, 48, -1888, 9000]
print("The list of numbers is:", numbers)
biggest = numbers[0]
for i in range (len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("Biggest number is:", biggest)



# Problem 4
# Use a while loop to print the numbers from 1 to 10.
print("--------------------Problem 4-----------------------------------------------")
i = 1
while i <= 10:
    print(i)
    i += 1



# Problem 5
# Create a function called count_above_10(numbers).
# It should return how many numbers in the list are above 10.
# Call it and print the result.
print("-------------------------------Problem 5-------------------------------------------------")
ref1 = 10
numbers2 = [8, 17, -18, 12, 21, 2, 4, 9]
print("The list of numbers is:", numbers2)
def count_above_10(numbers2):
    count = 0
    for i in range(len(numbers2)):
        if numbers2[i] > ref1:
            count += 1
    return count

print("The number of numbers above 10 are:", count_above_10(numbers2))
print("--------End of Lesson 1 Homework Problems--------------------")