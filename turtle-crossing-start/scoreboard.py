from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,level = 1):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.level = level
        self.write(f'level:{self.level}',font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.write(f'level:{self.level}', font=FONT)

    def reset(self):
        self.level = 1

    def declare_loss(self):
        self.clear()
        self.home()
        self.write(f'Game Over! Final Level {self.level}',align='center',font=FONT)
