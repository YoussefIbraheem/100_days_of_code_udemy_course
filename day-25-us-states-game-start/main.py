from turtle import Turtle , Screen
from PIL import Image
import pandas
from pandas import Series
import os

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
states_count = len(data.index)
game_on = True
score = 0

if os.path.exists("guessed_states.csv"):
    guessed_states = pandas.read_csv("guessed_states.csv")
else:
    print("No previous game data found. Starting a new game.")
    guessed_states = pandas.DataFrame(columns=["state", "x", "y"])

def save_guessed_states():
    guessed_states.sort_values(by="state", inplace=True)
    guessed_states.to_csv("guessed_states.csv", index=False)

def check_if_state_exists(state_input:str)-> Series or bool:
    is_state_exist = data[data["state"] == state_input.lower()]
    guessed_states_list = [state.lower() for state in guessed_states["state"].to_list()]
    if is_state_exist.empty:
        return False
    else:
        if state_input.lower() in guessed_states_list:
            print(f"You have already guessed {state_input}.")
            return False
        else:
            print(f"{state_input} is a correct answer.")
            return is_state_exist.iloc[0]

def add_correct_state_to_map(correct_state):
    state = Turtle(visible=False)
    state.penup()
    state.teleport(correct_state["x"] , correct_state["y"])
    state.write(correct_state["state"].title(), align="center", font=("Courier", 9, "bold"))
    if correct_state["state"] not in guessed_states["state"].to_list():
        guessed_states.loc[len(guessed_states)] = [correct_state["state"].title(), correct_state["x"], correct_state["y"]]
        save_guessed_states()


def announce(player_status:str):
    announcement = Turtle(visible=False)
    announcement.penup()
    announcement.goto(0, 0)
    if player_status == "winner":
        print("You have won the game.\n")
        print(f"Your score is {score}/{states_count}")
        announcement.write("You have won the game!", align="center", font=("Courier", 16, "bold"))
    elif player_status == "loser":
        print("You have lost the game.\n")
        print(f"Your score is {score}/{states_count}")
        announcement.write("You have lost the game!", align="center", font=("Courier", 16, "bold"))
    else:
        print("Invalid player status.")
        announcement.write("Invalid player status.", align="center", font=("Courier", 16, "bold"))

if not guessed_states.empty:
    for index, state in guessed_states.iterrows():
       add_correct_state_to_map(state.to_dict())
       score += 1

while game_on:

    if score >= states_count:
        announce("winner")
        game_on = False

    answer = screen.textinput(f"Correct Answers {score}/{states_count}","Enter state name:")
    if answer is None:
        game_on = False
        save_guessed_states()
        screen.bye()
    else:
        processed_answer = check_if_state_exists(answer.strip())
        if processed_answer is False:
           continue
        else:
            add_correct_state_to_map(processed_answer)
            score +=1

screen.mainloop()