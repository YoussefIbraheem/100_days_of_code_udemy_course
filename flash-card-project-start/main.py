import random
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

import pandas as pa
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
FR_CARD = Image.open("./images/card_front.png")
BK_CARD = Image.open("./images/card_back.png")
RI_BTN = Image.open("./images/right.png")
WR_BTN = Image.open("./images/wrong.png")
words_to_learn_file_path = Path("./data/words_to_learn.csv")
current_card = {}

try:
    data = pa.read_csv(words_to_learn_file_path)
except FileNotFoundError:
    shutil.copy("./data/french_words.csv", "./data/words_to_learn.csv")
    data = pa.read_csv("./data/words_to_learn.csv")


words = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    if not words:
        messagebox.showinfo(
            "Bien joué!", "Félicitations, vous parlez maintenant couramment français!"
        )
        words_to_learn_file_path.unlink()
        root.destroy()
        return
    current_card = random.choice(words)
    card_canvas.itemconfig(card_bg, image=fr_card_img)
    card_canvas.itemconfig(card_language, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = root.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(card_bg, image=bk_card_img)
    card_canvas.itemconfig(card_language, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def word_known():
    words.remove(current_card)
    pa.DataFrame(words).to_csv(words_to_learn_file_path, index=False)
    next_card()



root = tk.Tk()
flip_timer = root.after(3000, flip_card)
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.geometry("1000x1000")
fr_card_img = ImageTk.PhotoImage(image=FR_CARD)
bk_card_img = ImageTk.PhotoImage(image=BK_CARD)
card_canvas = tk.Canvas(
    root,
    highlightthickness=0,
    borderwidth=0,
    bg=BACKGROUND_COLOR,
    width=FR_CARD.width,
    height=FR_CARD.height,
)
right_btn_img = ImageTk.PhotoImage(image=RI_BTN)
wrong_btn_img = ImageTk.PhotoImage(image=WR_BTN)
right_btn = tk.Button(
    image=right_btn_img,
    border=0,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    takefocus=0,
    command=word_known,
)
wrong_btn = tk.Button(
    image=wrong_btn_img,
    border=0,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    takefocus=0,
    command=next_card,
)
card_bg = card_canvas.create_image(0, 0, image=fr_card_img, anchor="nw")
card_language = card_canvas.create_text(
    FR_CARD.width // 2,
    FR_CARD.height // 2 - 100,
    text="",
    font=("Ariel", 40, "italic"),
    fill="black",
)
card_word = card_canvas.create_text(
    FR_CARD.width // 2,
    FR_CARD.height // 2,
    text="",
    font=("Ariel", 60, "bold"),
    fill="black",
)


card_canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

# init()
next_card()
root.mainloop()
