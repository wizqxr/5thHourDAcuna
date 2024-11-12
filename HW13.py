#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW13
import random

#1. Create a list containing 10 integers of your choice.
intList  = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for j in intList:
    if j % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
    print(j)
# Print the total count of even and odd numbers.
print("The amount of even numbers you have are", evenNumbers)
print("The amount of odd numbers you have are", oddNumbers)