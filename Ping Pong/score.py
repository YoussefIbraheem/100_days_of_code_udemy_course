from turtle import Turtle

class Score(Turtle):

    def __init__(self , player_type):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player_type = player_type
        self.score = 0
        self.setup_score()


    def setup_score(self):
        if self.player_type.lower() == 'player_1':
            self.teleport(-200, 250)
        elif self.player_type.lower() == 'player_2':
            self.teleport(200 , 250)
        else:
            raise ValueError("Player can only 'player_1' or 'player_2'")

        self.write(f"{self.player_type}: {self.score}", align="center", font=("Courier", 20, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.setup_score()

    def get_score(self):
        return self.score


    def announce_winner(self):
        self.clear()
        self.teleport(0, 0)
        self.write(f"{self.player_type} Wins!!", align="center", font=("Courier", 20, "normal"))

