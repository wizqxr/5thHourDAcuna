#Name: Dominic Acuna
#Class: 5th Hour
#Assignment: Playground
import random
import tkinter as tk
from gettext import install
from tkinter import font

import pip
import pygame


'''
name = (input("Hello, what is the name your choosing to be known as?"))
print("Nice to meet you,",name ,",What shall we do today?")
input()
print("That sounds great to do", name, "!")
print("Tell me a little about yourself!")
input()
print("Wow! Your a very interesting human being!")

riddleList = ["Yes", "No"]
print("Lemme tell you a riddle! Its a little odd but i'm sure you'll get it!")
print("Listen here all far and wide, for I am the greatest computer of all! Do you Deny?! Please say Yes or No not yes or no.")


x = input()
if x == "No":
    print("Good job! I thought I'd have to destroy your internet haha!")

elif x == "Yes":
    print("Sorry man but I gotta destroy your internet access. Goodbye :)")

else:
    print("You failed the riddle, you shall be destroyed.")


numList1 = [1, 5, 10, 15, 20]
numList2 = [100, 150, 200, 250, 300]

sum = numList1[0] + numList2[0] * numList1[4] * numList2[3] / numList1[3]
print(sum)

input("Would you like to hit the monster Zachy Poo?!~ (Yes or No)")


if x == "No":
    print("You run away.")

elif x == "Yes":
    print("You take a chance and swing your mega big and long sword")

else:
    print("he kills you because you did not attempt to flee or attack.")

import random

hitList = [1, 5, 10]

x = (random.choice(hitList))

print(x)

if x == 1:
    print("Hit!")

elif x == 5:
    print("Big Hit!")

else:
    print("Critical!")

'''


'''
def load_chamber():
    chamber = [0, 0, 0, 0, 0, 1]
    random.shuffle(chamber)
    return chamber

def pull_trigger(chamber):
    result = chamber.pop()
    return result

def play_russian_roulette():
    chamber = load_chamber()
    input("Press Enter to pull the trigger...")
    result = pull_trigger(chamber)
    if result == 1:
        print("You're dead!")
    else:
        print("You survived!")
        play_russian_roulette()

if __name__ == "__main__":
    play_russian_roulette()
'''


'''
class Player:
    def __init__(self, name):
        self.name = name

    def take_turn(self, chamber):
        input(f"{self.name}, press Enter to pull the trigger...")
        result = chamber.pop()
        if result == 1:
            print(f"{self.name} is dead!")
            return False
        else:
            print(f"{self.name} survived!")
            return True

def load_chamber():
    chamber = [0, 0, 0, 1, 0, 0]
    random.shuffle(chamber)
    return chamber

def play_russian_roulette(player1, player2):
    chamber = load_chamber()
    while chamber and player1.take_turn(chamber) and player2.take_turn(chamber):
        pass

player1 = Player("Player 1")
player2 = Player("Player 2")
play_russian_roulette(player1, player2)
'''


'''
userInput = input("Enter a phrase to put in the screen!")
window = tk.Tk()

window.title("My Window")

custom_font = font.Font(family="Arial", size=100, weight="bold")

window.geometry("1280x720")

label = tk.Label(window, text=userInput, font = custom_font)
label.pack()

window.mainloop()
'''


'''
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    ace_count = hand.count('A')
    total = 0
    for card in hand:
        if card in ['K', 'Q', 'J']:
            total += 10
        elif card == 'A':
            total += 11
        elif type(card) == int:
            total += card
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hands(player_hand, dealer_hand, hide_dealer=True):
    clear()
    print("Dealer's Hand:")
    if hide_dealer:
        print("[Hidden Card]", dealer_hand[1])
    else:
        print(*dealer_hand)
    print("Value:", calculate_hand_value(dealer_hand) if not hide_dealer else "?")
    print("\nYour Hand:", *player_hand)
    print("Value:", calculate_hand_value(player_hand))

def play_blackjack():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        display_hands(player_hand, dealer_hand)
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack!")
            break
        action = input("Hit or Stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            if calculate_hand_value(player_hand) > 21:
                display_hands(player_hand, dealer_hand, False)
                print("Bust!")
                break
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    if calculate_hand_value(player_hand) <= 21:
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
        display_hands(player_hand, dealer_hand, False)

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif player_value == dealer_value:
            print("Push!")
        else:
            print("You lose.")

if __name__ == "__main__":
    play_blackjack()
'''



