import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import  Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates
snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.get_heading().distance(food) < 15:
        scoreboard.increment_score()
        food.refresh()
        snake.extend_snake()
    if snake.get_heading().xcor() > 290 or snake.get_heading().xcor() < -290 or snake.get_heading().ycor() > 290 or snake.get_heading().ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.get_segments()[1:]:
        if snake.get_heading().distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()



