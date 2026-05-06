# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

root = Tk()
root.title("My Pass")
root.config(padx=50,pady=50)
root.resizable(width=False,height=False)
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo_img)
website_input = Entry(width=35)
website_label = Label(text="Website")
eu_input = Entry(width=35)
eu_label = Label(text="Email/Username")
password_input = Entry(width=21)
password_label = Label(text="Password")
gen_pass_btn = Button(text="Generate Password",width=14)
add_btn = Button(text="Add",width=35,padx=0)

website_label.grid(row=1,column=0)
eu_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
canvas.grid(row=0,column=1,columnspan=2,sticky="nsew")

