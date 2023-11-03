from turtle import Turtle, Screen
import random

ttl = Turtle()
ttl.shape("turtle")
ttl.color("red")
ttl.width(1)
screen = Screen()
screen.colormode(255)

# TODO: 1. draw a rectangle
# for i in range(4):
#     ttl.fd(100)
#     ttl.right(90)


# TODO: 2. draw a dashed line
# for i in range(15):
#     ttl.fd(10)
#     ttl.penup()
#     ttl.fd(10)
#     ttl.pendown()


# TODO: 3. draw a triangle, square, ... , and decagon
# for i in range(3, 11):
#     screen.colormode(255)
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     ttl.pencolor(tup)
#     ttl.color()
#     for j in range(i):
#         ttl.forward(100)
#         ttl.left(360 / i)


# # alternatively
# def draw(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         ttl.forward(100)
#         ttl.left(angle)
#
#
# for i in range(3, 11):
#     screen.colormode(255)
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     ttl.pencolor(tup)
#     ttl.color()
#     draw(i)


# # TODO: 4. draw a random walk
# ttl.pensize(10)
# ttl.speed("fastest")
#
# while True:
#     screen.colormode(255)
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     ttl.pencolor(tup)
#     ttl.fd(20)
#     ttl.left(90 * random.randint(1, 4))


# TODO: 5. make a spirograph
ttl.speed("fastest")
ttl.pensize(1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


def draw_circle(tilt):
    for _ in range(int(360 / tilt)):
        ttl.pencolor(random_color())
        ttl.circle(150)
        ttl.setheading(ttl.heading() + tilt)


draw_circle(5)
screen.exitonclick()
