#game.py file - this should run the rock paper scissors game

import random #for the computer's selection

#title - should print player's name
print("-------------------")
print("Welcome 'Player One' to Rock, Paper, Scissors, Shoot!")
print("-------------------")
choices = ["paper", "rock", "scissors"]

#asking for player's input
player_choice = input("Please choose 'rock', 'paper', or 'scissors':")

#validate user selection
player_choice.lower()

if player_choice not in choices:
    print("Oops, invalid input. Please try again.")
    exit()

print("You chose: " + player_choice)

#simulate computer choice
computer_choice = random.choice(choices)

print(f"The computer chose: {computer_choice}")

if computer_choice == "paper" and player_choice == "scissors":
    print("Congrats! You Won!")
elif computer_choice == "scissors" and player_choice == "rock":
    print("Congrats! You Won!")
elif computer_choice == "rock" and player_choice == "paper":
    print("Congrats! You Won!")
elif computer_choice == player_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. It's ok.")


print("-------------------")
print("Thanks for playing!")

exit()