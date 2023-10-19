print("The Love Calculator is calculating your score...")
name1 = input("Your name? ") # What is your name?
name2 = input("Their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_name = (name1 + name2).lower()

# calculating true/love score - version 1
# times_t = combined_name.count("t")
# times_r = combined_name.count("r")
# times_u = combined_name.count("u")
# times_e = combined_name.count("e")
# times_l = combined_name.count("l")
# times_o = combined_name.count("o")
# times_v = combined_name.count("v")
#
# score_true = times_t + times_r + times_u + times_e
# score_love = times_l + times_o + times_v + times_e

# calculating true/love score - version 2
score_true = 0
score_love = 0

for letter in "true":
    letter_count = combined_name.count(letter)
    score_true += letter_count

for letter in "love":
    letter_count = combined_name.count(letter)
    score_love += letter_count

# next step
final_score = int(str(score_true) + str(score_love))

if final_score > 90 or final_score < 10:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 <= final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")


