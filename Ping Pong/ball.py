from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self,screen_width , screen_height):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1)
        self.speed(1)
        self.first_bounce(screen_width , screen_height)

    def first_bounce(self,screen_width , screen_height):
        x_cor = random.choice([-screen_width,screen_width])
        y_cor = random.randint(-screen_height,screen_height)
        self.goto(x_cor , y_cor)
