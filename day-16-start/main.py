import turtle
from prettytable import PrettyTable


# timmy = turtle.Turtle()
#
# my_screen = turtle.Screen()
#
# print(timmy)
# timmy.color('green')
# timmy.shape("turtle")
# timmy.forward(25)
# timmy.backward(50)
#
#
# my_screen.canvheight = 100
# my_screen.canvwidth = 100
# my_screen.exitonclick()


table = PrettyTable()

table.align = "l"
table.field_names = ["Pokemon Name" , "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmandar", "Fire"])

print(table)