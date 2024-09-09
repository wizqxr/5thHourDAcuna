#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: Playground

name = (input("Hello, what is the name your choosing to be known as?"))
print("Nice to meet you,",name ,",What shall we do today?")
input()
print("That sounds great to do", name, "!")
print("Tell me a little about yourself!")
input()
print("Wow! Your a very interesting human being!")

riddleList = ["Yes", "No"]
print("Lemme tell you a riddle! Its a little odd but i'm sure you'll get it!")
print("Listen here all far and wide, for I am the greatest computer of all! Do you Deny?! Please say Yes or No not yes or no.")


x = input()
if x == "No":
    print("Good job! I thought I'd have to destroy your internet haha!")

elif x == "Yes":
    print("Sorry man but I gotta destroy your internet access. Goodbye :)")

else:
    print("You failed the riddle, you shall be destroyed.")


numList1 = [1, 5, 10, 15, 20]
numList2 = [100, 150, 200, 250, 300]

sum = numList1[0] + numList2[0] * numList1[4] * numList2[3] / numList1[3]
print(sum)

input("Would you like to hit the monster Zachy Poo?!~ (Yes or No)")


if x == "No":
    print("You run away.")

elif x == "Yes":
    print("You take a chance and swing your mega big and long sword")

else:
    print("he kills you because you did not attempt to flee or attack.")

import random

hitList = [1, 5, 10]

x = (random.choice(hitList))

print(x)

if x == 1:
    print("Hit!")

elif x == 5:
    print("Big Hit!")

else:
    print("Critical!")