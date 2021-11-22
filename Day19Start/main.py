# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# # def move_foreard():
# #     tim.forward(30)
# # screen.listen()
# # screen.onkey(key = 'space', fun = move_foreard)
# # screen.exitonclick()
# #
#
#
#
# def move_foreard():
#     tim.forward(30)
#
# def move_backward():
#     tim.backward(30)
#
# def move_clockwise():
#     tim.right(90)
#
# def move_counterclockwise():
#     tim.left(90)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key = 'W', fun = move_foreard)
# screen.onkey(key='S', fun=move_backward)
# screen.onkey(key = 'A', fun = move_counterclockwise)
# screen.onkey(key='D', fun=move_clockwise)
# clear()
# screen.exitonclick()







# Turtle race
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
y_pos = -70
all_turtles = []
for i in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos)
    y_pos += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You got it right, {winning_color} won")
            else:
                print(f"You lost, {winning_color} won")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()