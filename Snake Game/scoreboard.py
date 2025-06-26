from turtle import Turtle

class Scoreboard(Turtle):
    __FONT = "Courier"
    __ALIGNMENT = "center"

    def __init__(self):
        """Initializes the Scoreboard with default values and sets up the display."""
        super().__init__()
        self.__score = 0
        with open("data.txt", "r") as file:
            try:
                self.__highest_score = int(file.read())
                file.close()
            except ValueError:
                self.__highest_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setposition(0,275)
        self.refresh_board()

    def get_score(self):
        return self.__score

    def set_score(self,scr:int):
        self.__score = scr

    def get_highest_score(self):
        return self.__highest_score

    def set_highest_score(self,highest_score):
        self.__highest_score = highest_score
        with open("data.txt", "w") as file:
            file.write(str(self.__highest_score))
            file.close()



    def increment_score(self):
        self.__score += 1
        self.refresh_board()

    def refresh_board(self):
        self.clear()
        self.write(f"Score:{self.__score}", False, 'left', (self.__FONT, 18, "bold"))
        self.write(" " * 20, False, 'center', (self.__FONT, 18, "bold"))
        self.write(f"Highest Score:{self.__highest_score}", False, 'right', (self.__FONT, 18, "bold"))

    def game_over(self):
        self.clear()
        self.home()
        if self.get_score() > self.get_highest_score():
            self.set_highest_score(self.get_score())
        self.write("Game Over \n Highest Score: " + str(self.get_highest_score()), False, self.__ALIGNMENT, (self.__FONT, 18, "bold"))
