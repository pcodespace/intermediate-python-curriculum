word = "strawberry"
vowels = "aeiouy"
count = 0
for Madakasira in word:
    if Madakasira in vowels:
        count = count +1
print("Vowel count:", count)

test = "racecar"
if test == test[::-1]:
    print(test, "is a palindrome")
else:
    print(test, "is not a palindrome")

fruit = "banana"
result = ""
for Madakasira in fruit:
    if Madakasira != "a":
        result = result + Madakasira
print(result)