from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.goto(-230, 230)
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)

