from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_NUMBER_OF_CAR = 25


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if len(self.cars) < MAX_NUMBER_OF_CAR:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            x_cor = random.randint(320, 1120)
            y_cor = random.randint(-240, 240)
            car.goto(x=x_cor, y=y_cor)
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -320:
                self.cars.remove(car)

    def level_up(self):
        self.speed += MOVE_INCREMENT