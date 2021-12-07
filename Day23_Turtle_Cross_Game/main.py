import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()


screen.listen()
screen.onkey(player1.up, "Up")
cars = []
game_is_on = True
for i in range(0, 10):
    cars.append(CarManager())
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for i in range(0, 10):
        cars[i].move_backward()


