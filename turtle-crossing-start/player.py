from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.teleport(*STARTING_POSITION)
        self.setheading(90)


    def move_forward(self):
        if self.heading() != 90:
            self.setheading(90)
        self.goto(self.xcor() , self.ycor() + MOVE_DISTANCE)

    def move_backwards(self):
        if self.heading() != 270:
            self.setheading(270)
        self.goto(self.xcor() , self.ycor() - MOVE_DISTANCE)


    def reset(self):
        if self.heading() != 90:
            self.setheading(90)
        self.teleport(*STARTING_POSITION)
