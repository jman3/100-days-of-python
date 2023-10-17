import random
# 5 inputs
q1 = input("What's the name of the city where you grew up? ")
q2 = input("What's the color you like the most? ")
q3 = input("English word you like the most: ")
q4 = input("Your last name? ")
q5 = input("Random word you like to include: ")

name_list = [q1, q2, q3, q4, q5]
sampled_list = random.sample(name_list, 3)

band_name = " ".join(sampled_list)

print("Here's your band name created: " + band_name)
# pick 3 of them and generate the band name
