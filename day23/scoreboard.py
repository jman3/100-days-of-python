from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(x=-220, y=260)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
