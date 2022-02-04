'''
Author: acbart (2/6/2019)
Version: 1
Co-author: shrey (9/9/2021)

1. Give a brief description of how the code below works.
   Use plain, accessible language and avoid repeating
   the exact statements from the code. Aim to write at
   least 3 sentences.
   
   The code below, first asks for your name which is unique from user to user.
   Then the game aspect is choosing a number from 1 to 10, and it tells you how to get
   closer to the number after each guess. As the user keeps guessing the game keep guiding
   you, until that number is sucessfully guessed. 

2. Make a modification to the code in some place that changes the game
   in some interesting way. This cannot be as simple as changing the
   MINIMUM or one of the printed messages, but make enough changes and
   they can add up. You might allow the player to play more rounds after
   the first one, or completely change all the messages to have a pirate
   theme, or make it so the player can specify the maximum number.
   Describe your change here clearly and explain why you thought it was
   interesting.
   
   I changed the maximum number so it is harder for the user to guess the number
   which makes it more of a challenege. I modified the ending message a little bit as well,
   asking the user if they want to play again. I also reduced the minimum to 0.
   This is interesting because it will take more time
   for the player to guess the number and the fun goes on for longer. 

'''

# Import the randint function generate random integers
from random import randint

# Establish the lower and uppper bound on the goal number
Lowest = 0
Highest = 20

def print_welcome():
    '''
    Prompt the user for their charcter, and then display a
    simple message explaining the rules of the game.
    '''
    # Get the name of the user
    name = input("What is your charcter? ")
    # Show the user's name
    print("Hello", name, "and welcome to the Shreya's epic guessing game.")
    # Print out the limits of the goal number
    print("You have to choose a number between", Lowest, "and", Highest)
    # Write out rest of the instructions
    print("Try to guess that number to win.")
    print("I'll give you a clue until you have guessd it.")
     
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("You win! Care to go again?")
    
def process_guess(guess, goal):
    '''
    Print out whether or not the user was above, below,
    or at the goal.
    
    Args:
        guess (int): The number that the user entered
            as their guess.
        goal (int): The number that the computer is
            thinking of.
    '''
    # Branch execution based on whether the guess was right
    if guess < goal: 
        print("Higher")
    elif guess > goal:
        print("Lower")
    else:
        print("Correct, it's", goal)

def get_number():
    '''
    Ask the user for a number, and keep prompting
    them until they give you an actual number
    (as opposed to giving you a letter).
    '''
    # Get the guess from the user, returns a string
    number = input("What is your guess? ")
    # Was the string composed only of numbers?
    if number.isdigit():
        # If so, we can safely convert it to an integer
        number_as_int = int(number)
        # And return the result
        return number_as_int
    else:
        # Otherwise, call this function again recursively
        return get_number()

def main_game():
    '''
    Play a round of the game.
    '''
    # Pick random number between MINIMUM and MAXIMUM
    goal = randint(Lowest, Highest) 
    # Initially, the user hasn't guessed anything.
    user_guess = None

    print_welcome()
    # Repeatedly ask the user until they get it right
    while user_guess != goal:
        user_guess = get_number()
        process_guess(user_guess, goal)
    print_ending()

# This if statement is common in most professional Python
#   programs - don't worry too much about what it does,
#   but you can safely assume it will work when you press
#   the run button.
if __name__ == '__main__':
    main_game()