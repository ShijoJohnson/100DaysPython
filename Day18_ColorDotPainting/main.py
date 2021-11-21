#import colorgram
import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)
color_list = [(227, 233, 230), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#10 by 10 rows cols
#each dot 20 size spaced by 50
tim.penup()
tim.hideturtle()
tim.setpos(-250.00, -250.00)

for i in range(10):
    for j in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.backward(500)

screen = Screen()
screen.exitonclick()