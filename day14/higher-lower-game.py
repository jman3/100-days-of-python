from art import logo, vs
from game_data import data
import random


# game_data 에서 무작위로 인스타계정을 뽑는다 (뽑힌건 리스트에서 삭제)
def random_choice(game_data):
    choice_index = random.randint(0, len(game_data) - 1)
    choice = game_data.pop(choice_index)
    return choice


# 정답이 맞는지 체크한다
def check_answer(option_a, option_b):
    print(
        f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']} {option_a['follower_count']}")
    print(vs)
    print(
        f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']} {option_b['follower_count']}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    follower_a = option_a['follower_count']
    follower_b = option_b['follower_count']
    answer = follower_a >= follower_b

    if (answer and user_answer == "a") or (not answer and user_answer == "b"):
        return True
    else:
        return False

    # 위 if 문을 아래와 같이 작성할 수도 있다 (wow)
    # if follower_a > b_follower:
    #   return user_answer == "a"
    # else:
    #   return user_answer == "b"

# 정답이 맞다면 B는 A에 넣고 새로 인스타 계정을 뽑아서 B에 넣는다 (반복)
# 정답이 틀리다면 게임을 종료한다
def main():
    end_of_game = False
    score = 0
    while not end_of_game:
        if score == 0:
            # 로고를 프린트한다
            print(logo)
            option_a = random_choice(game_data=data)
        option_b = random_choice(game_data=data)
        if check_answer(option_a, option_b):
            option_a = option_b
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}.")


main()