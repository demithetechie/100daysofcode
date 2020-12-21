import turtle as t
from turtle import Screen
import random

isRacing = False
racer = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
s = Screen()
bet = s.textinput("Make your bet", "Who will win the race?")
userBet = True
print(bet)
x = -350
y = 100
all_turtles = []

for i in range(6):
    colour = racer[i]
    racer[i] = t.Turtle()
    racer[i].penup()
    racer[i].shape("turtle")
    racer[i].color(colour)
    racer[i].setposition(x, y)
    racer[i].speed(random.randint(1, 10))
    all_turtles.append(racer[i])
    y -= 25

if userBet:
    isRacing = True

while isRacing:
    for turtle in all_turtles:
        distance = random.randint(1, 10)
        turtle.forward(distance)
        if turtle.xcor() > 325:
            colour = turtle.color()
            winning_colour = colour[0]
            isRacing = False


if bet == winning_colour:
    print(f"Well done! The {winning_colour} turtle is the winner!")
else:
    print(f"You lose! The {winning_colour} turtle is the winner!")


s.exitonclick()