#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: HW3


#Print Hello World!
print("Hello World!")

#Create a list with 5 strings containing 5 different names in it
nameList = ["Dom", "Zachy Poo", "Jim", "Tim", "Bob"]
print(f"{nameList [1]}")

#Append a new name onto the Name List
nameList.append(input())

#Print out the 4th name on the list
print(f"{nameList [3]}")

#Create a list with 4 different intergers in it
numList = [2, 9, 0, 4]

#Insert a new interger into the 2nd spot
numList.insert(1, 75)

#Print the interger list
print(numList)

#Sort the list from lowest to highest
numList.sort()
print(numList)

#Add the 1st three numbers on the sorted list together
sum = numList[0] + numList[1] + numList[2]

#Print the sum
print(sum)