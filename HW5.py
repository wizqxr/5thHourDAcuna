#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW5

#1. Print "Hello World!"
print("Hello World!")

#2. Create a list that contains 3 integers
numList = [567, 700, 200]

#3. Create an if statement that prints out whichever of the three numbers is the highest
if numList[0] > numList[1] and numList[0] > numList[2]:
    print("The first number is the biggest number.")

elif numList[1] > numList[0] and numList[1] > numList[2]:
    print("The second number is the biggest number.")

else:
    print("The third number is the biggest number.")

print(numList)