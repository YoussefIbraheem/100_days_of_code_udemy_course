import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move_forward , 'w')
screen.onkey(player.move_backwards,'s')
carManager =CarManager('hard')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.move_cars()
    carManager.remove_cars()
    if carManager.cars_list[-1].xcor() < 250:
        carManager.generate_cars()



