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
initial_difficulty = 'easy'
carManager =CarManager(initial_difficulty)
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.move_cars()
    carManager.remove_cars()

    for car in carManager.cars_list:
        if car.distance(player) < 25:
            scoreboard.declare_loss()
            game_is_on = False
            screen.exitonclick()

    if carManager.cars_list[-1].xcor() < 250:
        carManager.generate_cars()

    if player.ycor() >= 260:
        scoreboard.increment_level()
        carManager.increase_difficulty()
        player.reset()



