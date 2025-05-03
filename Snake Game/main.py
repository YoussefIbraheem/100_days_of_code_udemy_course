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
    if snake.get_heading().xcor() > 280 or snake.get_heading().xcor() < -280 or snake.get_heading().ycor() > 280 or snake.get_heading().ycor() < -280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()



