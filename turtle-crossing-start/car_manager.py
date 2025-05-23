from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5

MOVE_INCREMENT = 10

DIFFICULTY = {
    'hard': {'x_steps': 100 , 'y_steps': 50},
    'medium': {'x_steps': 150 , 'y_steps': 75},
    'normal': {'x_steps': 200 , 'y_steps': 100},
    'easy': {'x_steps': 150 , 'y_steps': 100},
}

class CarManager:

    def __init__(self, difficulty = 'easy'):
        """
        Initializes the CarManager with a specified difficulty level.

        The difficulty level determines the speed and spacing of the cars.

        1. 'hard' - Cars move fast and are closely spaced.
        2. 'medium' - Cars move moderately fast and are moderately spaced.
        3. 'normal' - Cars move at a normal speed and are spaced normally.
        4. 'easy' - Cars move slow and are spaced far apart.
        """
        self.cars_list = []
        self.game_difficulty = DIFFICULTY[difficulty]
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.generate_cars()

    def generate_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        return car


    def generate_cars(self):
        for y_cor in range(-200, 250, self.game_difficulty['y_steps']):
            for x_cor in range(280, 500, self.game_difficulty['x_steps']):
                new_car = self.generate_car()
                new_car.goto(x_cor + random.randint(0, 30), y_cor + random.randint(-10, 10))
                self.cars_list.append(new_car)


    def move_cars(self):
        if len(self.cars_list) > 0:
            for car in self.cars_list:
                car.backward(self.cars_speed)
        else:
            raise ValueError("please generate cars first")



    def remove_cars(self):
        for car in self.cars_list:
            if car.xcor() < -320:
                self.cars_list.remove(car)


    def increase_difficulty(self):
        difficulty_order = ['easy', 'normal', 'medium', 'hard']
        current_index = difficulty_order.index(next(key for key, value in DIFFICULTY.items() if value == self.game_difficulty))
        if current_index < len(difficulty_order) - 1:
            self.game_difficulty = DIFFICULTY[difficulty_order[current_index + 1]]

    def reset_difficulty(self,initial_difficulty):
        self.game_difficulty = initial_difficulty


    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT