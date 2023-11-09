from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in self.starting_position:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.setposition(position)
            self.segments.append(segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            next_position = self.segments[segment - 1].position()
            self.segments[segment].goto(next_position)
        # 맨 처음에 있는 segment는 아래처럼 for loop 밖에서 이동시켜준다
        self.segments[0].forward(20)
