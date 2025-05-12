from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5

MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars_list = []
        self.generate_cars(20)
        self.position_cars()


    def generate_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        return car


    def generate_cars(self, cars_amount: int):
        excluded_x_cors = []
        excluded_y_cors = []
        for car in range(cars_amount):
            new_car = self.generate_car()
            x_cor_candidates = [cor for cor in range(300, 600) if all(abs(cor - x) > 100 for x in excluded_x_cors)]
            y_cor_candidates = [cor for cor in range(-250, 250) if all(abs(cor - y) > 100 for y in excluded_y_cors)]
            new_x_cor = random.choice( x_cor_candidates or [random.randint(300, 600)] )
            new_y_cor = random.choice( y_cor_candidates or [random.randint(-250, 250)] )
            excluded_x_cors.append(new_x_cor)
            excluded_y_cors.append(new_y_cor)
            self.cars_list.append(new_car)
            new_car.goto(new_x_cor, new_y_cor)


    def position_cars(self):
                if len(self.cars_list) > 0:
                    excluded_x_cors = []
                    excluded_y_cors = []
                    for car in self.cars_list:
                        new_x_cor = random.choice([cor for cor in range(-250, 250) if cor not in excluded_x_cors])
                        excluded_x_cors.append(new_x_cor - 20)
                        new_y_cor = random.choice([cor for cor in range(-250, 250) if cor not in excluded_y_cors])
                        excluded_y_cors.append(new_y_cor - 20)
                        car.goto(new_x_cor, new_y_cor)
                else:
                    raise ValueError("please generate cars first")



    def move_cars(self):
        if len(self.cars_list) > 0:
            for car in self.cars_list:
                car.setheading(180)
                car.forward(MOVE_INCREMENT)
        else:
            raise ValueError("please generate cars first")



    def remove_cars(self):
        for car in self.cars_list:
            if car.xcor() < -320:
                self.cars_list.remove(car)

