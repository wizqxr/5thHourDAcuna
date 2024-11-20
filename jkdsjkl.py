#Name: Dom Acuna
#Class: 5th Hour
#Assignment: HW14
import random

#1. Create a variable that asks the user for an integer and an empty intger variable.
j = int(input("Choose a number in between 1-10."))
r = 1
#2. Create a loop with a range from 1 to the number the user input.
for k in range(1, j + 1,):
    r *= k

print(r)
#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.1
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120

#4. Print the factorial.