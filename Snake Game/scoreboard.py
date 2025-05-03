from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.__score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(0,290)
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
        self.write(f"Score:{self.__score}", False, 'center', ("Arial", 18, "bold"))