#Name:Dom Acuna
#Class: 5th Hour
#Assignment: HW12
import time
import random



#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.


i = 5

for i in range(5, 0, -1):
    print(i)
    time.sleep(0.4)
else:
    print("Hello World!")


#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)


for r in range(1, 31):
    if r % 2 == 0:
        print(r)


#3. Create a for loop that prints 5 different animals from a list.


animals = ["elephant", "lion", "raccoon", "giraffe", "dragon"]

for d in animals:
    print(d)


#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")


for v in input("Type a word to spell backwards!")[::-1]:
    print(v)

