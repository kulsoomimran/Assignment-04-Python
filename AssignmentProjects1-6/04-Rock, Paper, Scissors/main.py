import random

def play():
    user = input("What's your choice?\n'r' for Rock,'p' for Paper and 's' for Scissors? ").lower()
    
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    
    if user not in choices:
        return "Invalid choice. Please select 'r', 'p', or 's'."
    
    user_choice = choices[user]
    
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    
    print(f"Computer chose: {computer}")

    if user_choice == computer:
        return "It's a tie!"

    if is_win(user_choice, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):

    # r > s, s > p, p > r

    if (player == "rock" and opponent == "scissors") or \
       (player == "scissors" and opponent == "paper") or \
       (player == "paper" and opponent == "rock"):
        return True

print(play())
    