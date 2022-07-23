from replit import clear
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False
print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if the
# chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in chosen_word:
    display.append('_')

# Loop through each position in the chosen_word;
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed the letter {guess}.")
        continue

    elif guess in chosen_word:
        # version 1
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
                print(' '.join(display))
                print(stages[lives])

        # version 2
        # for idx in range(len(chosen_word)):
        #     if chosen_word[idx] == guess:
        #         display[idx] = guess

    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives <= 0:
            print("You lose.")
            end_of_game = True

        print(' '.join(display))
        print(stages[lives])

    # Check if the player wins
    if '_' not in display:
        end_of_game = True
        print("You win.")
