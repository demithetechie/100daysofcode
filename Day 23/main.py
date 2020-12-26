import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
c = CarManager()
level = Scoreboard()
count = 0

screen.listen()
screen.onkey(p.move, "Up")
game_is_on = True

while game_is_on:
    count += 1
    if count % 6 == 0:
        c.generate_cars()
    time.sleep(0.1)
    screen.update()
    c.move()
    for car in c.cars:
        if car.distance(p) < 25:
            game_is_on = False
            level.game_over()
    if p.ycor() > FINISH_LINE_Y:
        level.update()
        p.goto(STARTING_POSITION)
        c.increase_speed()

screen.exitonclick()
