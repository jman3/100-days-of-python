# import modules
from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# set a difficulty level of the game
def set_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# check if user's guess matches the answer
# deduct 1 to user's turns if they get it wrong
def check_guess(guess, answer, turns):
    if guess > answer:
        print("Too high")
        turns -= 1
    elif guess < answer:
        print("Too low")
        turns -= 1
    else:
        print(f"You got it right. The answer was {answer}.")
    return turns


#  print logo
def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # choose a random number between 1 and 100
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # set user's remaining turns
    turns = set_level()

    # repeat guess & check until the game's over
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


main()
