import random
import math
choices = ["rock", "paper", "scissors"]

player = None
player_score = 0
computer_score = 0
games_to_play=int(input("Enter how many games you wish to play: "))
games_played=0
games_needed_to_win=math.ceil(games_to_play/2)

while player_score != games_needed_to_win or computer_score != games_needed_to_win:
    computer = random.choice(choices)
    print("Player score is: ", player_score)
    print("Computer score is: ", computer_score)
    if player_score == games_needed_to_win:
        print("PLAYER WINS!!!")
        break
    elif computer_score == games_needed_to_win:
        print("COMPUTER WINS...")
        break

    player = input("rock, paper, scissors: ").lower()
    if player not in ["rock", "paper", "scissors"]:
        print("Enter valid choice!!!!")
    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")
        games_played+=1
        print("Games played: ",games_played)
        

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")
            games_played+=1
            print("Games played: ",games_played)
            player_score += 0
            computer_score += 1
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")
            games_played+=1
            print("Games played: ",games_played)

            player_score += 1
            computer_score += 0
    # -----------------------------------------------------------------------#
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")
            games_played+=1
            print("Games played: ",games_played)

            player_score += 1
            computer_score += 0
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")
            games_played+=1
            print("Games played: ",games_played)

            player_score += 0
            computer_score += 1
    # -----------------------------------------------------------------------#
    elif player == "scissors":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player wins")
            games_played+=1
            print("Games played: ",games_played)

            player_score += 1
            computer_score += 0
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins")
            games_played+=1
            print("Games played: ",games_played)

            player_score += 0
            computer_score += 1
