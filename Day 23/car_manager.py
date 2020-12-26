from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.distance = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT
        self.cars = []
        self.initialise_cars()

    def initialise_cars(self):
        for i in range(10):
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.cars.append(car)
            random_y = random.randint(-250, 250)
            random_x = random.randint(250, 300)
            random_col = random.choice(COLORS)
            car.color(random_col)
            car.goto(random_x, random_y)

    def generate_cars(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        self.cars.append(car)
        random_y = random.randint(-250, 250)
        random_x = random.randint(250, 300)
        random_col = random.choice(COLORS)
        car.color(random_col)
        car.goto(random_x, random_y)

    def move(self):
        for car in self.cars:
            car.backward(self.distance)

    def increase_speed(self):
        self.distance += self.increment


