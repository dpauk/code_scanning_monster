"""Rock, paper, scissors game between a humna and a computer"""

import sys

import random

POSSIBLE_GUESSES = ['rock', 'paper', 'scissors']

def get_computer_guess():
    """Generates a random guess from the computer"""
    computer_guess = POSSIBLE_GUESSES[random.randint(0, 2)]
    print("Computer guesses: {}".format(computer_guess.capitalize()))
    return computer_guess

def is_human_guess_valid(human_guess):
    """Test to see if a human guess is between 1 and 3"""
    try:
        human_guess = int(human_guess)
    except ValueError:
        raise ValueError
    guess_valid = True
    if human_guess < 1 or human_guess > 3:
        guess_valid = False
    return guess_valid

def get_human_guess():
    """Displays the instructions and gets the human's guess"""
    print(
        """Possible guesses:
        1 = Rock
        2 = Paper
        3 = Scissors
        """
    )
    human_guess = input("Please enter your guess: ")

    try:
        if not is_human_guess_valid(human_guess):
            print("Invalid guess.")
            sys.exit(1)
    except ValueError:
        print("Invalid guess.")
        sys.exit(1)

    return POSSIBLE_GUESSES[int(human_guess) - 1]

def get_winner(human_guess, computer_guess):
    """Works out who the winner is"""
    if (human_guess == "rock" and computer_guess == "rock") or\
        (human_guess == "paper" and computer_guess == "paper") or\
        (human_guess == "scissors" and computer_guess == "scissors"):
        print("Both have chosen the same.")
        return "It's a draw!"
    elif (human_guess == "rock" and computer_guess == "scissors") or\
        (human_guess == "paper" and computer_guess == "rock") or\
        (human_guess == "scissors" and computer_guess == "paper"):
        print("You have chosen {}, Computer has chosen {}".format(human_guess.capitalize(), computer_guess.capitalize()))
        return "You win!"
    else:
        print("You have chosen {}, Computer has chosen {}".format(human_guess.capitalize(), computer_guess.capitalize()))
        return "Computer wins!"

def main():
    """The main body of the game"""
    human_guess = get_human_guess()
    computer_guess = get_computer_guess()
    winner = get_winner(human_guess, computer_guess)
    print(winner)

if __name__ == '__main__':
    main()
