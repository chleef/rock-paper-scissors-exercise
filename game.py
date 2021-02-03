#game.py file - this should run the rock paper scissors game

import random

#title - should print player's name
print("-------------------")
print("Welcome 'Player One' to Rock, Paper, Scissors, Shoot!")
print("-------------------")

#asking for player's input
player_choice = input("Please choose 'rock', 'paper', or 'scissors':")

print("You chose: " + player_choice)

#simulate computer choice
choices = ["paper", "rock", "scissors"]
computer_choice = random.choice(choices)

print(f"The computer chose: {computer_choice}")

exit()