import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
t.colormode(255)

def random_color():
    red =   random.randint(0,255)
    green = random.randint(0, 255)
    blue =  random.randint(0,255)
    color = (red , green , blue)
    return color

def draw_shape(shape):
    for i in range(3,shape):
        axis = int(360 / i)
        timmy.color(random.choice(random_color()))
        for j in range(i):
            timmy.right(axis)
            timmy.forward(180)
        timmy.home()
    Screen().exitonclick()


def random_walk(times):
    timmy.pensize(15)
    timmy.speed("fastest")
    for i in range(times):
        random_axis = random.choice([0,90,180,270])
        random_length = random.randint(10, 100)
        timmy.color(random_color())
        timmy.setheading(random_axis)
        timmy.forward(random_length)
    Screen().exitonclick()


def spirograph(gap):
    timmy.speed("fastest")
    for i in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(120)
        timmy.setheading(i * gap)
    Screen().exitonclick()
