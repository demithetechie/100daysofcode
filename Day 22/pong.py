from turtle import Turtle


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.75, stretch_len=5)
        self.color("white")
        self.shape("square")
        self.setheading(270)
        self.st()
        self.penup()

    def player1position(self):
        self.setposition(280, 0)

    def player2position(self):
        self.setposition(-280, 0)

    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



