from turtle import Turtle , Screen

class Player(Turtle):



    def __init__(self,player_type:str,screen_width , screen_height):
        super().__init__()
        self.screen = Screen()
        self.screen.listen()
        self.player_x_cor = (screen_width / 2) - 50
        self.player_y_cor = 0
        self.player_type = player_type
        self.set_player()

    def setup_player(self):
        self.shape('square')
        self.color('White')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def set_player(self):
        self.setup_player()
        if  self.player_type.lower() == 'player_1':
            self.teleport(self.player_x_cor * -1,self.player_y_cor)
            self.screen.onkey(self.move_up,'w')
            self.screen.onkey(self.move_down, 's')
        elif self.player_type.lower() == 'player_2':
            self.teleport(self.player_x_cor , self.player_y_cor)
            self.screen.onkey(self.move_up, 'Up')
            self.screen.onkey(self.move_down, 'Down')
        else:
            raise ValueError("Wrong input: player_type must be 'player_1' or 'player_2'")

    def move_up(self):
        self.goto(self.xcor() , self.ycor() + 40)

    def move_down(self):
        self.goto(self.xcor() , self.ycor() - 40)

