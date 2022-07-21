rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

options = [rock, paper, scissors]

# user and computer choose what to throw
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# check if an invalid number has been entered
if user_choice < 0 or user_choice > 2:
    print('You typed an invalid number, you lose!')
else:
    # let computer choose a random number between 0 and 2
    com_choice = random.randint(0, 2)
    # print out user's choice and com's choice
    print(options[user_choice])
    print('Computer chose:\n', options[com_choice])

    # 3. determine who won and print out the result
    if user_choice == com_choice:
        print("It's a draw")
    elif user_choice == 0 and com_choice == 2:
        print("You win!")
    elif user_choice == 2 and com_choice == 0:
        print("You lose")
    elif user_choice > com_choice:
        print("You win!")
    else:
        print("You lose")
