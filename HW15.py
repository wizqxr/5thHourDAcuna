#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW15
import random
import time


#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")

#2. Create a def function that calculates the average of three numbers.
def calculate_average(num1, num2, num3):

    average = (num1 + num2 + num3) / 3
    print(num1, num2, num3)
    print(average)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*fuhuh):
    print("This animal is", fuhuh[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def print_numbers(n):

  for i in range(1, n + 1):
    time.sleep(0.4)
    print(i)

#5. Call all of the functions created in 1 - 4 with relevant arguments.
