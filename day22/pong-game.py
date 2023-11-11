from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_over = False
while not game_is_over:
    time.sleep(ball.ball_speed)
    ball.ball_move()
    screen.update()

    # detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.ball_bounce_y()

    # detect collision with paddles
    if (ball.xcor() < -330 and ball.distance(l_paddle) < 50) or (ball.xcor() > 330 and ball.distance(r_paddle) < 50):
        ball.ball_bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
