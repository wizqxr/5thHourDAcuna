#Name: Dom Acuna
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.


#Make The Dictionary

enemyDict = {
"Zacharious": {
     "Type" : "Electric",
    "Health" : 1000,
    "Damage" : 110,
    "Stamina" : 100,
    "Attack Effects" : "Stun"

},
"The Great Gabrius": {
     "Type" : "Lean",
    "Health" : 500,
    "Damage" : 100,
    "Stamina": 75,
    "Attack Effects": "Drunk"

},
"Skibidi Jonques": {
     "Type" : "Water",
    "Health" : 250,
    "Damage" : 75,
    "Stamina": 80,
    "Attack Effects": "Slow"

},
"Dommy Knocker": {
     "Type" : "Earth",
    "Health" : 2000,
    "Damage" : 150,
    "Stamina": 150,
    "Attack Effects": "Stun"

},
"The Black Wonder": {
     "Type" : "Darkness",
    "Health" : 5000,
    "Damage" : 300,
    "Stamina": 250,
    "Attack Effects": "Blind"

},
}
print(enemyDict)

#Damage change for Zacharious
newDamageA = input("Enter new Damage Points for Zacharious: ")
enemyDict["Zacharious"]["Damage"] = newDamageA

#Damage change for The Great Gabrius
newDamageB = input("Enter new Damage Points for The Great Gabrius: ")
enemyDict["The Great Gabrius"]["Damage"] = newDamageB

#Damage change for Skibidi Jonques
newDamageC = input("Enter new Damage Points for Skibidi Jonques: ")
enemyDict["Skibidi Jonques"]["Damage"] = newDamageC

#Damage change for Dommy Knocker
newDamageD = input("Enter new Damage Points for Dommy Knocker: ")
enemyDict["Dommy Knocker"]["Damage"] = newDamageD

#Damage change for The Black Wonder
newDamageE = input("Enter new Damage Points for The Black Wonder: ")
enemyDict["The Black Wonder"]["Damage"] = newDamageE

#Printing the new changes

print("Print new changes?")

x = input()

if x == "No":
    print("Okay!")

elif x == "Yes":
    print("Alright printing now.")
    print(("Zacharious = "), enemyDict["Zacharious"]["Damage"], ("DP"))
    print(("The Great Gabrius = "), enemyDict["The Great Gabrius"]["Damage"], ("DP"))
    print(("Skibidi Jonques = "), enemyDict["Skibidi Jonques"]["Damage"],("DP"))
    print(("Dommy Knocker = "), enemyDict["Dommy Knocker"]["Damage"], ("DP"))
    print(("The Black Wonder = "), enemyDict["The Black Wonder"]["Damage"], ("DP"))


else:
    print("Error")




