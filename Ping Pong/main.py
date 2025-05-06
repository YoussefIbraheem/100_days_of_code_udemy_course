from turtle import Screen
from player import Player
from ball import Ball

screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(screen_width , screen_height)
screen.bgcolor('Black')
player_1 = Player('player_1',screen_width , screen_height)
player_2 = Player('player_2',screen_width , screen_height)
ball = Ball()
game_on = True

while game_on:
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380 :
        ball.reset_position()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()



screen.exitonclick()
