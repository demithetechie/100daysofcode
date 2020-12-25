from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# setting up the t
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


screen.tracer(0)


s = Snake()
f = Food()
score = ScoreBoard()

screen.onkeypress(s.up, "Up")
screen.onkeypress(s.down, "Down")
screen.onkeypress(s.left, "Left")
screen.onkeypress(s.right, "Right")
screen.listen()
GameOn = True

while GameOn:
    screen.update()
    s.move()

    # Detect collision with snake and food
    if s.head.distance(f) < 15:
        s.grow()
        f.refresh()
        score.increment_score()

    # Detect collision with wall
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        # GameOn = False
        score.reset()
        s.reset()
        # score.game_over()

    # Detect collision with tail
    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            # GameOn = False
            score.reset()
            s.reset()
            # score.game_over()

    time.sleep(0.1)

# replay = screen.textinput("Play again?", "Would you like to play again? Type 'y' for yes, and 'n' for no.")
# if replay == 'y':
#     GameOn = True

screen.exitonclick()
