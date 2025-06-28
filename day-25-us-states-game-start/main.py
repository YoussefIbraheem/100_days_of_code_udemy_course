from turtle import Turtle , Screen
from PIL import Image
import pandas
from pandas import Series

turtle = Turtle()
screen = Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"

with Image.open(image) as img:
    img_width ,  img_height = img.size

screen.addshape(image)
turtle.shape(image)
screen.setup(img_width , img_height)

def get_screen_coordinates(x,y):
    print(x,y)

screen.onscreenclick(get_screen_coordinates)

data = pandas.read_csv("50_states.csv")

data["state"] = data["state"].str.lower()

game_on = True
score = 0

def check_if_state_exists(state_input:str):
    is_state_exist = data[data["state"] == state_input.lower()]
    if is_state_exist.empty:
        return None
    else:
        return  is_state_exist

def add_correct_state_to_map(correct_state:Series):
    state_data = correct_state.iloc[0].to_dict()
    state = Turtle(visible=False)
    state.penup()
    state.teleport(state_data["x"] , state_data["y"])
    state.write(state_data["state"].upper(), align="center", font=("Courier", 9, "bold"))



def announce(player_status:str):
    announcement = Turtle(visible=False)
    announcement.penup()
    announcement.goto(0, 0)
    if player_status == "winner":
        print("You have won the game.\n")
        print(f"Your score is {score}/50")
        announcement.write("You have won the game!", align="center", font=("Courier", 16, "bold"))
    elif player_status == "loser":
        print("You have lost the game.\n")
        print(f"Your score is {score}/50")
        announcement.write("You have lost the game!", align="center", font=("Courier", 16, "bold"))
    else:
        print("Invalid player status.")
        announcement.write("Invalid player status.", align="center", font=("Courier", 16, "bold"))

while game_on:
    if score >= 50:
        announce("winner")
        game_on = False

    answer = screen.textinput(f"Correct Answers {score}/50","Enter state name:")
    if answer is None:
        game_on = False
        screen.bye()
    else:
        processed_answer = check_if_state_exists(answer)
        if processed_answer is None:
           announce("loser")
           game_on = False
        else:
            add_correct_state_to_map(processed_answer)
            score +=1

screen.mainloop()