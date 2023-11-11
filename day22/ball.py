from turtle import Turtle

START_BALL_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.ball_speed = START_BALL_SPEED

    def ball_move(self):
        new_x = self.xcor() + (10 * self.x_direction)
        new_y = self.ycor() + (10 * self.y_direction)
        self.goto(new_x, new_y)

    def ball_bounce_y(self):
        self.y_direction *= -1
        self.ball_speed *= 0.9

    def ball_bounce_x(self):
        self.x_direction *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.x_direction *= -1
        self.ball_speed = START_BALL_SPEED
