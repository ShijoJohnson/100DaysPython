from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        #self.penup()
        self.goto(280, (-260 + (random.randint(20, 100) * STARTING_MOVE_DISTANCE)))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        # while self.xcor() > -340:
        # #    self.move_backward()
        #     self.backward(5)
    def move_backward(self):
        if self.xcor() > -340:
            self.backward(10)




