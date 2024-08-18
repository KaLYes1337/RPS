import random

choices = ["rock", "paper", "scissors"]

player = None
player_score = 0
computer_score = 0

while player_score != 3 or computer_score != 3:
    computer = random.choice(choices)
    print("Player score is: ", player_score)
    print("Computer score is: ", computer_score)
    if player_score == 3:
        print("PLAYER WINS!!!")
        break
    elif computer_score == 3:
        print("COMPUTER WINS...")
        break

    player = input("rock, paper, scissors: ").lower()
    if player != "rock" or "paper" or "scissors":
        print("Enter valid choice!!!!")
    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")

            player_score += 0
            computer_score += 1
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")

            player_score += 1
            computer_score += 0
    # -----------------------------------------------------------------------#
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")

            player_score += 1
            computer_score += 0
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")

            player_score += 0
            computer_score += 1
    # -----------------------------------------------------------------------#
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")

            player_score += 1
            computer_score += 0
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")

            player_score += 0
            computer_score += 1
