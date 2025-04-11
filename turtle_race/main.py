import turtle
import random

def setup_screen(width, height):
    screen = turtle.Screen()
    screen.setup(width=width, height=height)
    return screen

def get_user_bet(colors):
    bet = turtle.textinput("Place your bet!", f"Which turtle will win the race? Enter a color from {colors}:")
    return bet.lower() if bet else None

def create_turtles(players, start_x, gap):
    turtles = {}
    half_count = (len(players) - 1) / 2
    for index, (name, color) in enumerate(players.items()):
        t = turtle.Turtle(shape="turtle")
        t.color(color)
        t.penup()
        y_position = (half_count - index) * gap
        t.goto(start_x, y_position)
        turtles[name] = {'turtle': t, 'color': color}
    return turtles

def start_race(turtles, finish_line):
    while True:
        for player in turtles.values():
            t = player['turtle']
            t.forward(random.randint(0, 10))
            if t.xcor() >= finish_line:
                return player['color']

def main():
    screen_width, screen_height = 500, 400
    players = {
        'tim': 'blue',
        'neo': 'green',
        'luke': 'red',
        'lilly': 'pink',
        'stella': 'purple',
        'judas': 'cyan',
        'mo': 'brown'
    }

    screen = setup_screen(screen_width, screen_height)
    colors = list(players.values())
    user_bet = get_user_bet(colors)

    if user_bet not in colors:
        print("Invalid color selected.")
        return

    start_x = -screen_width / 2 + 20
    gap = screen_height / (len(players) + 1)
    turtles = create_turtles(players, start_x, gap)
    finish_line = screen_width / 2 - 20

    winning_color = start_race(turtles, finish_line)

    if winning_color == user_bet:
        print(f"Your turtle ({winning_color}) won! Congratulations!")
    else:
        print(f"The winning turtle is {winning_color}. Better luck next time!")

    screen.exitonclick()

if __name__ == "__main__":
    main()
