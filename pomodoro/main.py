import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
marks_count = ""
timer_loop = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global marks_count
    reps = 0
    marks_count=""
    start_button["state"] = "normal"
    
    marks.config(text=marks_count)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    root.after_cancel(timer_loop)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    start_button["state"] = "disabled"
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Long Break",fg=RED)
        countdown(long_break_sec)  # long break
    elif reps % 2 == 0:
        timer_label.config(text="Short Break",fg=PINK)
        countdown(short_break_sec) # short break
    else:
        timer_label.config(text="Work",fg=GREEN)
        countdown(work_sec) # work


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global marks_count
    global timer_loop
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(tagOrId=timer_text, text=f"{count_min}:{count_sec}")
        timer_loop = root.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 3 == 0:
            marks_count +="✔"
            marks.config(text=marks_count)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
tomato_img = PhotoImage(file="tomato.png")
start_button = Button(
    text="Start",
    fg=GREEN,
    bg="white",
    font=(FONT_NAME, 10, "bold"),
    command=start_timer,
)
reset_button = Button(text="Reset", fg=GREEN, bg="white", font=(FONT_NAME, 10, "bold"),command=reset_timer)
marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)

timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1, padx=50, pady=50)
start_button.grid(row=2, column=0)
marks.grid(row=2, column=1)
reset_button.grid(row=2, column=2)

root.mainloop()
