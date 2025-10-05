#Build “rock-paper-scissors” game in Python. 
# In this game, there are two players, user and bot named “RPS-3PO”.

#Rules for the RPS game:

    #Rock beats scissors
    #Paper beats rock
    #Scissors beat paper

#ASCII Art below for the game.

#In this exercise, place the following at the beginning of the code (right at the top). 
# Setting the seed value means we are setting an initial state for the random number 
# generator. After this, the generated numbers will follow exactly the same sequence. 
# The random number will then depend on the number of calls to the random function.

#import random
#random.seed(1234)

#Randomize the bot’s choice in each game by calling the random.randint(1, 3) function 
# with the given arguments. This function call returns a random integer between 1 and 3,
# inclusive. Implementing randomness in another way may lead to varying test results 
# and is therefore not recommended.

#The program start by asking for the player’s name. Then, greet the player and announce 
# the opponent. After that, inform that the game is starting.

#The menu contains 4 options, first three are game related options. If user chooses rock,
#paper or scissors from the menu, a round will be played.

#Display text "Rock! Paper! Scissors! Shoot!\n". Then, reveal the player’s choice first,
#followed by the bot’s choice. Show a decorative line of 25 hash (#) symbols between 
# and around the choices to visually separate the player’s and the bot’s selections.

#Then check the players’ choice according to the rules of the RPS game. 
# If both players have chosen the same option, the result is a draw 
# ("Draw! Both players chose ____."). Otherwise, declare the winner and the reason for 
# the victory based on the condition.

import random
random.seed(1234)

# ASCII-kuvat
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


ascii_art = ["", rock, paper, scissors]
names = ["", "rock", "paper", "scissors"]

def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")

    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

# Tilastot
    player_wins = 0
    player_losses = 0
    player_draws = 0

    bot_wins = 0
    bot_losses = 0
    bot_draws = 0

    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = int(input("Your choice: "))

        if choice == 0:
            break  #Poistutaan

        if choice not in (1, 2, 3):
            continue  #Takaisin alkuun

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")

        print("#" * 25)
        print(f"{player_name} chose {names[choice]}.\n")
        print(ascii_art[choice])
        print("#" * 25)

    #BOT
        print(f"RPS-3PO chose {names[bot_choice]}.\n")
        print(ascii_art[bot_choice])
        print("#" * 25)
        print()

    #Tasuri
        if choice == bot_choice:
            print(f"Draw! Both players chose {names[choice]}.\n")
            player_draws += 1
            bot_draws += 1

        elif (choice == 1 and bot_choice == 3) or \
            (choice == 2 and bot_choice == 1) or \
            (choice == 3 and bot_choice == 2):

        # Pelaaja voittaa
            print(f"{player_name} {names[choice]} beats RPS-3PO {names[bot_choice]}.\n")
            player_wins += 1
            bot_losses += 1

        else:
        # Botti voittaa
            print(f"RPS-3PO {names[bot_choice]} beats {player_name} {names[choice]}.\n")
            bot_wins += 1
            player_losses += 1

# Lopputulos
    print("\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"RPS-3PO - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})")
    
print("\nProgram ending.")

if __name__ == "__main__":
    main()