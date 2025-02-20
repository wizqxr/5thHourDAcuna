#Name:Dom Acuna
#Class: 5th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(l)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    y = int(input("Please choose a number!!!"))
    x = 100/y
    print(x)

except:
    print("Divided by 0 no bueno")


#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    i = int(input("Please choose a number!!!"))

except ValueError:
    print("error number is not integer")


#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
r = 5
while r >= 0:
    print(r)
    r -= 1
    if r < 0:
        raise Exception("gleeker mode")