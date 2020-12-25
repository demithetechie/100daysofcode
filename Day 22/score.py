from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 50, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        self.color("white")

    def position_score(self, pos):
        self.goto(pos)
        self.display_score()

    def display_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.display_score()
