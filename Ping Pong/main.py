from turtle import Screen
from fence import Fence
from player import Player
from ball import Ball

screen = Screen()
screen_width = 500
screen_height = 500
screen.setup(screen_width , screen_height)
screen.bgcolor('Black')
fence = Fence(screen_height)
player_1 = Player('player_1',screen_width , screen_height)
player_2 = Player('player_2',screen_width , screen_height)
ball = Ball(screen_width , screen_height)
screen.exitonclick()
