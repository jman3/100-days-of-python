from replit import clear
import random
from hangman_art import stages, logo
from hangman_words import word_list

# word_list 에서 임의의 단어를 하나 선택해서 chosen_word에 넣는다
chosen_word = random.choice(word_list)
# 플레이어의 라이프를 6으로 설정한다
lives = 6
end_of_game = False
print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# chosen_word 문자 개수 만큼 '_'를 넣을 리스트 display 를 만든다
display = []
for _ in chosen_word:
    display.append('_')

# List comprehension 을 이용해서 아래와 같이 만들 수도 있다
# display = ['_' for char in chosen_word]

# Loop through each position in the chosen_word;
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# end_of_game이 True가 될 때까지 단어를 추측하는 것을 반복한다.
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    # 만약 이미 입력했던 문자라면 피드백을 주고 다시 입력을 하도록 만든다
    if guess in display:
        print(f"You've already guessed the letter {guess}.")
        continue

    # 이미 입력했던 문자가 아니라면 여기까지 오게 된다.
    # 만약 입력한 문자가 정답에 포함되어 있는 문자라면, underscore(_)를 입력한 문자로 바꿔서 display에 넣어준다.
    # version 1 - enumerate 사용
    elif guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
        print(f'The guessed letter {guess} is in the answer!')
        print(stages[lives])
        print(' '.join(display))


    # version 2 - range 사용
    # for idx in range(len(chosen_word)):
    #     if chosen_word[idx] == guess:
    #         display[idx] = guess

    # 만약 입력한 문자가 정답에 포함되어 있지 않다면 오답 피드백을 주고 라이프를 1 감소시킨다
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        print(' '.join(display))

        # 만약 라이프가 0 이하가 되면 게임이 종료되므로 end_of_game 변수에 True를 할당하고 게임 종료를 알린다
        if lives <= 0:
            print("You lose.")
            end_of_game = True

    # 만약 단어가 완성되었다면 end_of_game 변수에 True를 할당하고 게임 승리를 알린다
    if '_' not in display:
        end_of_game = True
        print("You win.")
