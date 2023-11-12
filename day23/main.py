import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    if player.ycor() > 280:
        player.reset_turtle()
        cars.level_up()
        scoreboard.add_score()

    for car in cars.cars:
        if player.distance(car) < 18:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()