import random

def get_choices():
    player_choice = input("Enter a choice : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices  = {"player" : player_choice, "computer" : computer_choice}

    return choices

def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
       return "its a tie!"
    elif player == "rock" and computer == "paper" :
       return "Computer wins"
    elif player == "rock" and computer == "scissors" :
       return "Player wins"
    elif player == "paper" and computer == "scissors" :
       return "Computer wins"
    elif player == "paper" and computer == "rock" :
       return "Player wins"
    elif player == "scissors" and computer == "paper" :
       return "Player wins"
    elif player == "scissors" and computer == "rock" :
       return "Computer wins"

choices = get_choices()
player = choices["player"]
computer = choices["computer"]
result = check_win(player, computer)
print(result)