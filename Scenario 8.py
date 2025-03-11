#Name: Dom Acuna
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)



class Character:
    def __init__(self, name, attack_modifier, health, damage_range, ac):
        self.name = name
        self.attack_modifier = attack_modifier
        self.health = health
        self.damage = random.randint(*damage_range)
        self.ac = ac

    def __repr__(self):
        return f"{self.name} (HP: {self.health}, DMG: {self.damage}, AC: {self.ac}, ATK MOD: {self.attack_modifier})"


# Creating enemy characters
enemies = [
    Character("The Great Gabrius", 4, 12, (3, 8), 14),
    Character("Skibidi Jonques", 6, 17, (3, 6), 13),
    Character("Dommy Knocker", 5, 12, (1, 20), 15),
    Character("The Black Wonder", 7, 25, (5, 10), 17)
]

# Creating party characters
party = [
    Character("LaeZel", 7, 8, (1, 6), 17),
    Character("Shadowheart", 5, 19, (3, 8), 15),
    Character("Gale", 6, 17, (1, 10), 13),
    Character("Astarion", 4, 12, (5, 10), 14)
]

# Printing characters for verification
for enemy in enemies:
    print(enemy)

for member in party:
    print(member)



class Character:
    def __init__(self, name, attack_modifier, health, damage_dice, ac):
        self.name = name
        self.attack_modifier = attack_modifier
        self.health = health
        self.damage_dice = damage_dice
        self.ac = ac

    def roll_damage(self):
        if isinstance(self.damage_dice, tuple):
            return sum(random.randint(self.damage_dice[0], self.damage_dice[1]) for _ in range(self.damage_dice[2]))
        return random.randint(self.damage_dice[0], self.damage_dice[1])

    def __repr__(self):
        return f"{self.name}: Attack Modifier={self.attack_modifier}, Health={self.health}, AC={self.ac}"


party = {
    "Lae'Zel": Character("Lae'Zel", 7, 8, (1, 6, 2), 17),
    "Shadowheart": Character("Shadowheart", 5, 19, (3, 8, 1), 15),
    "Gale": Character("Gale", 6, 17, (1, 10, 1), 13),
    "Astarion": Character("Astarion", 4, 12, (5, 10, 1), 14)
}

# Example usage:
for character in party.values():
    print(f"{character.name} deals {character.roll_damage()} damage!")

