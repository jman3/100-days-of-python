from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# # snake 클래스 생성 전 코드 (abstraction 전)
# squares = []
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_position:
#     square = Turtle(shape="square")
#     square.color("white")
#     square.penup()
#     square.setposition(position)
#     squares.append(square)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # # snake 클래스 생성 전 코드 (abstraction 전)
    # for square_num in range(len(squares) - 1, 0, -1):
    #     next_position = squares[square_num - 1].position()
    #     squares[square_num].goto(next_position)
    # # 맨 처음에 있는 square는 아래처럼 for loop 밖에서 이동시켜준다
    # squares[0].forward(20)

screen.exitonclick()