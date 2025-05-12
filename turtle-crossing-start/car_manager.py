from turtle import Turtle
import random

class CarManager:

    __COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

    __STARTING_MOVE_DISTANCE = 5

    __MOVE_INCREMENT = 10

    def __init__(self,cars_amount):
        self.generate_cars(cars_amount=cars_amount)


    def __generate_car(self, position):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(self.__COLORS))
        car.teleport(position)

    def generate_cars(self, cars_amount:int):
        for _ in range(cars_amount):
            position = (280 , random.randint(-280,280))
            self.__generate_car(position)





