#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: Scenario 7
import random
#Import all of Scenario 6 here
def roll_stat():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort(reverse=True)
    return sum(rolls[:3])


stats = []


for _ in range(6):
    stats.append(roll_stat())


print("Character Stats:", stats)





listAverage = 0

def final_average():
    global listAverage
    listAverage = average = sum(stats) / len(stats)
    print(f"Average Stat: {average:.2f}")#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)