from turtle import Screen, Turtle
from pong import Pong
from ball import Ball
from score import Score
import time
import random

# set up screen
screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.tracer(0)

# draw dashed line in middle of screen
dashed_line = Turtle()
dashed_line.goto(0, 340)
dashed_line.setheading(270)
dashed_line.ht()
dashed_line.pensize(3)
dashed_line.color("white")
reached_end = False
while not reached_end:
    dashed_line.penup()
    dashed_line.forward(15)
    dashed_line.pendown()
    dashed_line.forward(15)
    if dashed_line.ycor() < -330:
        reached_end = True

# Set up game objects
p1 = Pong()
p2 = Pong()
b = Ball()
p1.player1position()
p2.player2position()
p1_score = Score()
p2_score = Score()
p1score_pos = (-40, 280)
p2score_pos = (40, 280)
p1_score.position_score(p1score_pos)
p2_score.position_score(p2score_pos)
GameOn = True

# pong board movement
screen.listen()
screen.onkeypress(p1.up, "Up")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p2.down, "s")


while GameOn:
    time.sleep(b.move_speed)
    screen.update()
    b.moveup()
    if b.xcor() > 350:
        p1_score.increment()
        b.padbounce()
        b.goto(0, 0)
        b.move_speed = 0.005
    elif b.xcor() < -350:
        p2_score.increment()
        b.padbounce()
        b.goto(0, 0)
        b.move_speed = 0.005
    elif b.ycor() > 330 or b.ycor() < -325:
        b.bounce()
    elif b.distance(p1) < 50 and b.xcor() > 265:
        b.padbounce()
    elif b.distance(p2) < 50 and b.xcor() < -265:
        b.padbounce()




screen.exitonclick()

# TODO Set up Screen with black background and dimensions
# TODO Create dashed line across the middle of the screen. Use a turtle for this.
# TODO Create a class for the pong boards which will inherit from the Turtle Class. Use separate file for this
# TODO Create a class for the ball which will inherit from the Turtle class
# TODO Detect collision with ball and either paddle
# TODO Detect ball collision with wall and bounce back
# TODO Create a scoreboard class for both players, increment when ball goes past x boundary for either player
# TODO After each round spawn ball in the middle of the screen with random direction towards either player
# TODO End game when either player score reaches 3

