#Name:
#Class: 5th Hour
#Assignment: Scenario 4
import random
#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.


#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
players = int(input("Enter a number of players."))
sum = 0
i = 0
while i < players:
    i += 1
    starRating = int(input("Enter a star rating between 1 and 5."))
    if starRating > 5 or starRating < 1:
        i -= 1
        print("ERROR")
        continue
    else:
        sum = sum + starRating

print(sum / players)

