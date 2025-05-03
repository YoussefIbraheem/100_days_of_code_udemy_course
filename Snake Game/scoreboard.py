from turtle import Turtle

class Scoreboard(Turtle):
    __FONT = "Courier"
    __ALIGNMENT = "center"

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(0,275)
        self.refresh_board()

    def get_score(self):
        return self.__score

    def set_score(self,scr:int):
        self.__score = scr

    def increment_score(self):
        self.__score += 1
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.write(f"Score:{self.__score}", False, self.__ALIGNMENT, (self.__FONT, 18, "bold"))

    def game_over(self):
        self.clear()
        self.home()
        self.write("Game Over", False, self.__ALIGNMENT, (self.__FONT, 24, "bold"))