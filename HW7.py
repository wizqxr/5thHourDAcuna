#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")

#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
userValue = 0

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
x = input("Connect to Internet? ")

if x == "Yes" or x == "yes":
    print("Alright your connected! Enter your username! ")
    userName = input()
elif x == "No" or x == "no":
    print("Goodbye. ")
    exit()
else:
    print("Error, couldn't understand your answer. ")
    exit()


if wifi:
    if login:
        if admin:
         print("Welcome",userName,"!")
         userValue += 1
         print("Online Users: ",userValue)
        else:
            print("Error, you are missing admin access.")
    else:
        print("Error, you are missing the login credentials.")
else:
    print("Error, you are not connected to the internet.")

