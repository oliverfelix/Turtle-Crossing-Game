from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.new_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle('square')
            # new_car.setheading(270)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_y = random.randint(-280,280)
            new_car.penup()
            new_car.goto(250, new_y)
            self.new_cars.append(new_car)

    def move_car(self):
        for i  in self.new_cars:
            i.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









