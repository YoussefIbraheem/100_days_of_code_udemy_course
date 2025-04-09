import colorgram
import random
from turtle import Turtle , Screen
extracted_colors = colorgram.extract('hirst.jpg',30)

turtle = Turtle()
Screen().colormode(255)

colors = []

for extracted_color in extracted_colors:
    red = extracted_color.rgb.r
    green = extracted_color.rgb.g
    blue = extracted_color.rgb.b
    color_tuple = (red,green,blue)
    if (255,255,255)  > color_tuple > (240,240,240):
        continue
    else:
        colors.append(color_tuple)

def hirst_drawing(num_of_dots = 10,gap = 50 , dot_size = 20):
    turtle.speed("fastest")
    turtle.penup()
    for i in range(num_of_dots):
        turtle.goto(-225, float(i * gap) -225)
        for _ in range(num_of_dots):
            random_color = random.choice(colors)
            turtle.dot(dot_size , random_color)
            turtle.forward(gap)
    Screen().exitonclick()


hirst_drawing()