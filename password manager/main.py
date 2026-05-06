import random
from tkinter import *
from tkinter import messagebox
from pathlib import Path
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    
    pass_nums = [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    pass_syms = [random.choice(symbols) for _ in range(0, random.randint(2, 4))]
    pass_letters = [random.choice(letters) for _ in range(0, random.randint(2, 4))]
    
    password_comp = pass_nums + pass_syms + pass_letters
    random.shuffle(password_comp)
    password = "".join(password_comp)
    pyperclip.copy(password)
    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    if not website:
        messagebox.showwarning("Missing Data", "Website is required")
        return

    eu = eu_input.get()
    if not eu:
        messagebox.showwarning("Missing Data", "Username/Email is required")
        return

    password = password_input.get()
    if not password:
        messagebox.showwarning("Missing Data", "Password is required")
        return

    file_path = Path("./data.txt")

    file_path.touch(exist_ok=True)

    with file_path.open(mode="a", encoding="utf-8") as f:
        f.write(f"{website} | {eu} | {password}\n")
        messagebox.showinfo("Success", "Password saved successfully")

    website_input.delete(0, END)
    password_input.delete(0, END)
    eu_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("My Pass")
root.config(padx=50, pady=50)
root.resizable(width=False, height=False)
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
website_input = Entry(width=35)
website_input.focus()
website_label = Label(text="Website")
eu_input = Entry(width=35)
eu_input.insert(0, "youssef@mail.com")
eu_label = Label(text="Email/Username")
password_input = Entry(width=21)
password_label = Label(text="Password")
gen_pass_btn = Button(text="Generate Password", width=14, font=("Arial", 8, "normal"), command=generate_password)
add_btn = Button(text="Add", width=35, padx=0, command=save_password)

website_label.grid(row=1, column=0)
eu_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
canvas.grid(row=0, column=1, columnspan=2)
website_input.grid(row=1, column=1, columnspan=2)
eu_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1, sticky="w")
gen_pass_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)
root.mainloop()
