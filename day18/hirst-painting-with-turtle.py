import random
from turtle import Turtle, Screen

# import colorgram
#
# colors = colorgram.extract('hirst-painting.jpeg', 30)
#
# color_list = []
# for color in colors:
#     colors_in_img = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_list.append(colors_in_img)

# 너무 배경색에 가까운 흰색 계열은 삭제하고 아래 컬러들로 진행
list_of_colors = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188),
                  (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251),
                  (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9),
                  (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160),
                  (10, 97, 61), (5, 38, 33), (67, 219, 155)]

# 10 by 10 rows of spots
# dot size 20 & distance between dots 50

ttl = Turtle()
screen = Screen()
screen.colormode(255)
ttl.speed("fastest")
ttl.hideturtle()


def draw_dot(rgb):
    ttl.dot(20, rgb)
    ttl.fd(50)


x = -225
y = -225
ttl.pu()
for _ in range(10):
    ttl.goto(x, y)
    for i in range(10):
        color = random.choice(list_of_colors)
        draw_dot(color)
    y += 50

screen.exitonclick()
