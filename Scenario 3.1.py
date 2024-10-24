#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: Scenario 3

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4
import random

#Step 1: Copy enemy dictionary from SC1
enemyDict = {
"The Great Gabrius": {
     "Attack Modifier" : 4,
    "Health" : 12,
    "Damage" : random.randint(3,8),
    "AC": 14
},
"Skibidi Jonques": {
     "Attack Modifier": 6,
    "Health" : 17,
    "Damage" : random.randint(3, 6),
    "AC": 13
},
"Dommy Knocker": {
     "Attack Modifier": 5,
    "Health" : 12,
    "Damage" : random.randint(1, 20),
    "AC": 15
},
"The Black Wonder": {
     "Attack Modifier" : 7 ,
    "Health" : 25,
    "Damage" : random.randint(5, 10),
    "AC" : 17
},
}

#Step 2: Copy party dictionary from SC2
partyDict = {
    "LaeZel" : {
        "Attack Modifier": 7,
        "Health": 8,
        "Damage": random.randint(1, 6) + random.randint(1,6) + 3,
        "AC": 17
    },
    "Shadowheart" : {
        "Attack Modifier": 5,
        "Health": 19,
        "Damage": random.randint(3, 8),
        "AC": 15
    },
    "Gale" : {
        "Attack Modifier": 6,
        "Health": 17,
        "Damage": random.randint(1, 10),
        "AC": 13
    },
    "Astarion" : {
        "Attack Modifier": 4,
        "Health": 12,
        "Damage": random.randint(5, 10),
        "AC": 14
    }
}
#Step 3: Make sure every enemy and party member has health points (fixed)
#Done
#Step 4: Make sure every enemy and party member has an attack modifier (fixed)
#Done
#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)
#Done
#Step 6: Make every enemy and party member has a damage roll (random)
#Done

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member (LaeZel)

#Step 8: Pick an ememy (Dommy Knocker)

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive


#Combat Code Goes Here
number = random.randint(1,20) + partyDict["LaeZel"]["Attack Modifier"]

print('Press ENTER to roll the die to attack enemy.')

if input()=='':

    print(number)

if number >= enemyDict["Dommy Knocker"]["AC"]:
    enemyDict["Dommy Knocker"]["Health"] -= partyDict["LaeZel"]["Damage"]
    print("Successful hit, the enemy's health is now ", enemyDict["Dommy Knocker"]["Health"])
    if enemyDict["Dommy Knocker"]["Health"] <= 0:
        print("The enemy has fallen."),
    else:
        print("Enemy is still alive"),
else:
    print("Attack Missed")
#SWAP EVERYTHING AROUND
if enemyDict["Dommy Knocker"]["Health"] > 0:
    number = random.randint(1, 20) + enemyDict["Dommy Knocker"]["Attack Modifier"]

    print('Press ENTER to roll the die to attack party member.')

    if input() == '':
        print(number)

    if number >= partyDict["LaeZel"]["AC"]:
        partyDict["LaeZel"]["Health"] -= enemyDict["Dommy Knocker"]["Damage"]
        print("Successful hit, the party members health is now ", partyDict["LaeZel"]["Health"])
        if partyDict["LaeZel"]["Health"] <= 0:
            print("The party member has fallen."),
            exit()
        else:
            print("Party member is still alive"),
    else:
        print("Attack Missed")




        #DONE!