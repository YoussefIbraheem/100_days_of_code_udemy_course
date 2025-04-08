from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(50):
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    timmy.forward(5)



Screen().exitonclick()
