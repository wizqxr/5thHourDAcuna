#Name: Dom Acuna
#Class: 5th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Charc:
    def __init__(self, health, damage, speed, max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health
    def damage_ot(self):
        for i in range(1, 10):
            self.health -= random.randint(1, 6)
            time.sleep(1)
            print("The New Health for the self is:", self.health)
    def healer(self):
        self.health += 30
        if self.health > self.max_health:
            self.health = self.max_health
            print("self is at its max health.")
        else:
            print(f"The self final health is: {self.health}")


#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Charc(100,20,30,100)
healer = Charc(60,10,30,60)
thief = Charc(50,10,30,50)
mage = Charc(45,35,25,45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
x = random.randint(1,4)
if x == 1:
    warrior.damage_ot()
elif x == 2:
    healer.damage_ot()
elif x == 3:
    thief.damage_ot()
elif x == 4:
    mage.damage_ot()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if warrior.health < warrior.max_health:
    warrior.healer()
    print("Warrior got hit! New health for WARRIOR is", warrior.health)
elif healer.health < healer.max_health:
    healer.healer()
    print("Healer got hit! New health for HEALER is", healer.health)
elif thief.health < thief.max_health:
    thief.healer()
    print("Thief got hit! New health for THIEF is", thief.health)
elif mage.health < mage.max_health:
    mage.healer()
    print("Mage got hit! New health for MAGE is", mage.health)