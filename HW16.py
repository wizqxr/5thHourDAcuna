#Name:Dominic Acuna
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand
playerscore = 0
def rps_game():
    playerchoice = int(input("Choose 1 for rock, 2 for paper, 3 for scissors."))
    opponentchoice = random.randint(1,3)
    global playerscore


    if playerchoice == 1 and opponentchoice == 2:
        print(f"Opponent chose {opponentchoice}")
        print("Opponent won with paper against your rock.")
        playerscore -= 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 1 and opponentchoice == 3:
        print(f"Opponent chose {opponentchoice}")
        print("You won against scissors with your rock.")
        playerscore += 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 2 and opponentchoice == 1:
        print(f"Opponent chose {opponentchoice}")
        print("You won against rock with your paper.")
        playerscore += 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 2 and opponentchoice == 3:
        print(f"Opponent chose {opponentchoice}")
        print("Opponent won with scissors against your paper.")
        playerscore -= 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 3 and opponentchoice == 1:
        print(f"Opponent chose {opponentchoice}")
        print("Opponent won with rock against your scissors.")
        playerscore -= 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 3 and opponentchoice == 2:
        print(f"Opponent chose {opponentchoice}")
        print("You won against paper with your scissors.")
        playerscore += 1
        print(f"Your score is now", playerscore)
    elif playerchoice == 1 and opponentchoice == 1:
        print(f"Opponent chose {opponentchoice}")
        print("Tied with both rocks.")
        print(f"Your score is still", playerscore)
    elif playerchoice == 2 and opponentchoice == 2:
        print(f"Opponent chose {opponentchoice}")
        print("Tied with both paper.")
        print(f"Your score is still", playerscore)
    elif playerchoice == 3 and opponentchoice == 3:
        print(f"Opponent chose {opponentchoice}")
        print("Tied with both scissors.")
        print(f"Your score is still", playerscore)
    else:
        print("Invalid input please choose a number between 1-3.")
        rps_game()
    replay_rps()



#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def replay_rps():
    replayInput = input("Would you like to play again? Y/N ")

    if replayInput == "Y" or replayInput == "y":
        rps_game()
    elif replayInput == "N" or replayInput == "n":
        exit()
    else:
        print("Invalid input")
        replay_rps()


rps_game()