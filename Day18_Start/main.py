# import turtle
import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
tim.color("red")
# move = 3
# angle = 120
#
# for i in range(7):
#     for j in range(move):
#         tim.forward(75)
#         tim.right(angle)
#     move += 1
#     angle -= angle / move
#

    # move = 3
    # angle = 120
    # moves += 1
    # angle -= angle/move
    #
    # 3, 120
    # 4, 90
    # 5, 72
    # 6, 60

# screen = Screen()
# screen.exitonclick()

# import heroes
# print(heroes.gen())
#

# Dashed Line
# for i in range(50):
#     tim.forward(5)
#     if i%2 == 0:
#         tim.penup()
#     else:
#         tim.pendown()

from random import choice

def get_random_number():
    return choice(range(1, 5))

tim.width(width = 1)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


# random walk
# directions = [45,70,20,30.50]
# while True:
#     dir = get_random_number()
#     tim.color(random_color())
#     if dir == 1:
#         tim.forward(random.choice(directions))
#     elif dir == 2:
#         tim.backward(random.choice(directions))
#     elif dir == 3:
#         tim.right(90)
#         tim.forward(random.choice(directions))
#     else:
#         tim.right(90)
#         tim.backward(random.choice(directions))


# spirograph
tim.speed('fastest')
for i in range(36):
    tim.circle(80)
    tim.right(10)
    tim.color(random_color())

screen = Screen()
screen.exitonclick()

