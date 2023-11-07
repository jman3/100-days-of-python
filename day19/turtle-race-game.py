import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

is_race_on = True

x = -230
y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40
    turtles.append(new_turtle)

print(turtles)

while is_race_on:
    for turtle in turtles:
        random_steps = random.randint(0, 10)
        turtle.forward(random_steps)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if user_bet == winning_turtle_color:
                print(f"You've won! The {winning_turtle_color} turtle won the race!")
            else:
                print(f"You've lost! The {winning_turtle_color} turtle won the race!")

screen.exitonclick()
