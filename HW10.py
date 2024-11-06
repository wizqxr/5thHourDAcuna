#Name: Dom Acuna
#Class: 5th Hour
#Assignment: HW10
import time
import random
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.

i = 5
while i >= 0:
    print(i)
    time.sleep(0.4)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.

l = 0
while l <= 30:
    time.sleep(0.2)
    l += 1
    if l % 2 == 0:
        print(l)

#3. Create a while loop that repeats until the user
#inputs the number 0.

r = int(input("Enter a number."))
while r != 0:
    print(r)
    r = int(input("Enter another number."))

#EXTRA STUFF

j = random.randint(0,10)

while j != 0:
    time.sleep(0.2)
    print(j)
    j = random.randint(0,10)

