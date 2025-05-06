import time
from turtle import Screen
from player import Player
from ball import Ball
from score import Score
screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(screen_width , screen_height)
screen.bgcolor('Black')
player_1_score = Score('player_1')
player_2_score = Score('player_2')
player_1 = Player('player_1',screen_width)
player_2 = Player('player_2',screen_width)
ball = Ball()
max_score = 10
game_on = True

while game_on:

    if player_1_score.get_score() >= max_score:
        player_1_score.announce_winner()
        game_on = False

    if player_2_score.get_score() >= max_score:
        player_2_score.announce_winner()
        game_on = False

    time.sleep(ball.movement_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        player_1_score.add_point()

    if ball.xcor() < -380:
        ball.reset_position()
        player_2_score.add_point()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()



screen.exitonclick()
