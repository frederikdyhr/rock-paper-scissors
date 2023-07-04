import random

# Variables to keep track of scores, games played and defining options for the player/computer
player_wins = 0
computer_wins = 0
games_played = 0
options = ("rock", "paper", "scissors")  # Options available to player and computer

# Welcome and rules
print("======== ROCK, PAPER, SCISSORS - BEST OF THREE - BY FREDERIK ========\n")
print("The rules are simple: \nRock crushes scissors, scissors cut paper, and paper covers rock.\nThe first to win 2 games wins the match!\n")

# Game continues until a player has won twice
while max([player_wins, computer_wins]) < 2:
    print("--------------------------------------------------------------------")
    print(f"======================= ROUND {games_played + 1} =======================")

    # Variables for player and computer choice (rock, paper or scissors)
    player = None  # Reset player choice each round
    computer = random.choice(options)  # Computer chooses randomly from the options

    # Prompt player for their choice until they give a valid option
    while player not in options:
        player = input("\nWhat is your play? (rock, paper or scissors):\n").lower()

    # Overview of player and computer play for round
    print(f"\nYour play: {player}")
    print(f"Computer's play: {computer}")

    # Increment games played counter
    games_played += 1

    # Determine and print result of round (win, tie or loss)
    print("\n--- ROUND RESULT ---")
    if player == computer:  # Case for a tie
        print("It's a tie!\n")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win this round!\n")
        player_wins += 1  # Increment player wins counter
    else:  # Remaining scenarios are all losses for the player
        print("You lose this round!\n")
        computer_wins += 1  # Increment computer wins counter

    # Print current match status
    print("Match status:")
    print(f"Rounds played: {games_played}")
    print(f"Your wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Rounds needed to win the match: {2 - max(player_wins, computer_wins)}\n")

# Determine and print match winner
if player_wins > computer_wins:
    print("\nCONGRATULATIONS! YOU WON THE MATCH.")
else:
    print("\nBETTER LUCK NEXT TIME. THE COMPUTER DEFEATED YOU.")

print("\n**THANKS FOR PLAYING! SEE YOU NEXT TIME :-)**")
