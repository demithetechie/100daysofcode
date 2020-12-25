from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.st()
        self.penup()
        self.goto(0, 0)
        self.x_move = 1
        self.y_move = 1
        self.speeds = 1
        self.move_speed = 0.005

    def moveup(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.speed(self.speeds)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 1.05

    def padbounce(self):
        self.x_move *= -1
        self.move_speed *= 1.05



