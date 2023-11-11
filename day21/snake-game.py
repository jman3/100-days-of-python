from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # 부동소수점 때문인지 distance를 사용하지 않고 position == 조건을 사용하면 가끔 작동하지 않는 때가 있었다
    if snake.head.distance(food) < 1:
        food.set_food_position()
        scoreboard.change_score()
        snake.extend()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280 or snake.is_collide():
        is_game_over = True
        scoreboard.game_over()

screen.exitonclick()