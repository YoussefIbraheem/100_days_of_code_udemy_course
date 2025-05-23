import time
from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.penup()
        self.movement_speed = 0.1
        self.move_x = 10
        self.move_y = 10
        self.move()


    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.movement_speed *= 0.9

    def move(self):
        x_cor = self.xcor() + self.move_x
        y_cor = self.ycor() + self.move_y
        self.goto(x_cor , y_cor)

    def reset_position(self):
        self.teleport(0,0)
        time.sleep(0.1)
        self.bounce_x()
        self.movement_speed = 0.1

