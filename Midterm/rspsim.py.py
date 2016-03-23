# Copyright (c) 2011 Cuong Ngo
# Rock, paper, and scissors between two computer

import random

WEAPON = ["scissors", "rock", "paper"]
rounds = 0
win1 = 0
win2 = 0
while rounds != 10:
    rounds += 1
    player1 = random.choice(WEAPON)
    player2 = random.choice(WEAPON)
    print("Round " + str(rounds) + ":")
    print(" HAL picks", player1 + ".")
    print(" WOPR picks", player2 + ".")
    if player1 == player2:
        print(" It's a tie.")
    elif player1 == "rock" and player2 == "scissors":
        print(" HAL wins.")
        win1 += 1
    elif player1 == "rock" and player2 == "paper":
        print(" WORP wins.")
        win2 += 1
    elif player1 == "paper" and player2 == "rock":
        print(" HAL wins.")
        win1 += 1
    elif player1 == "paper" and player2 == "scissors":
        print(" WORP wins.")
        win2 += 1
    elif player1 == "scissors" and player2 == "rock":
        print(" WORP wins.")
        win2 += 1
    elif player1 == "scissors" and player2 == "paper":
        print(" HAL wins.")
        win1 += 1
print("Final Score:")
print(" HAL won", win1)
print(" WOPR won", win2)
if win1 == win2:
    print(" It's a tie.")
elif win1 > win2:
    print(" HAL wins.")
elif win2 > win1:
    print(" WOPR wins.")
input("\n\nPress enter key to exit.")
