from turtle import Turtle

class Fence(Turtle):

    def __init__(self,screen_height):
        super().__init__()
        self.fence_y_cor = (screen_height / 2) - 50
        self.setup_fence()

    def setup_fence(self):
        self.color('white')
        self.hideturtle()
        self.pensize(5)
        self.penup()
        self.goto(0, self.fence_y_cor)
        self.setheading(270)  # Face downward
        self.draw_dashed_line()

    def draw_dashed_line(self):
        while self.ycor() > - self.fence_y_cor:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
