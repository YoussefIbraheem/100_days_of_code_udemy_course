import time
from turtle import Screen
from food import Food
from snake import  Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates
snake = Snake()
food = Food()

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
        print("nom nom nom")
        food.refresh()


screen.exitonclick()



