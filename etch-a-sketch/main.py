from turtle import *

screen = Screen()
timmy = Turtle()

screen.setup(700,700)

def move_forward():
    timmy.forward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def move_backwards():
    timmy.backward(10)

def clear():
    timmy.penup()
    timmy.home()
    timmy.clear()
    timmy.pendown()


onkey(move_forward,"w")
onkey(turn_left,"a")
onkey(turn_right,"d")
onkey(move_backwards,"s")
onkey(clear,"c")

listen()

screen.exitonclick()
