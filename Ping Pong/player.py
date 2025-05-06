from turtle import Turtle , Screen

class Player(Turtle):



    def __init__(self,player_type:str,screen_width , screen_height):
        super().__init__()
        self.screen = Screen()
        self.screen.listen()
        self.player_x_cor = (screen_width / 2) - 50
        self.player_y_cor = (screen_height / 2) - 150
        self.player_type = player_type
        self.set_player()

    def setup_player(self):
        self.shape('square')
        self.color('White')
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)

    def set_player(self):
        self.setup_player()
        if  self.player_type.lower() == 'player_1':
            self.teleport(self.player_x_cor * -1,self.player_y_cor)
            self.screen.onkeypress(self.move_up,'w')
            self.screen.onkeypress(self.move_down, 's')
        elif self.player_type.lower() == 'player_2':
            self.teleport(self.player_x_cor , self.player_y_cor)
            self.screen.onkeypress(self.move_up, 'Up')
            self.screen.onkeypress(self.move_down, 'Down')
        else:
            raise ValueError("Wrong input: player_type must be 'player_1' or 'player_2'")

    def emit_player_position(self):
        print(f"{self.player_type}: {self.position()}")

    def move_up(self):
        self.sety(self.ycor() + 20)
        self.emit_player_position()

    def move_down(self):
        self.sety(self.ycor() - 20)
        self.emit_player_position()

