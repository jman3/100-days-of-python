from art import logo
import random


# function to set a difficulty
def set_level():
    """ This function is for setting up the level of the game """
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == "easy":
        return 10
    elif game_level == "hard":
        return 5


def check_guess():
    global end_of_game, life
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        end_of_game = True
    elif guess > answer:
        print("Too high!")
        life -= 1
    else:
        print("Too low!")
        life -= 1
    if not end_of_game:
        print(f"You have {life} attempts remaining to guess the number.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
print(answer)

life = set_level()
end_of_game = False
print(f"You have {life} attempts remaining to guess the number.")

while life > 0 and end_of_game == False:
    check_guess()

if life == 0:
    print("You've run out of guesses, you lose.")
    end_of_game = True