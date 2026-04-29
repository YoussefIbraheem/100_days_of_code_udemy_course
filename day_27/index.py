from tkinter import *

root = Tk()
root.title("Miles To Kilometers Converter")
root.config(padx=20, pady=20)
input = Entry(width=10)
miles_indicator = Label(text="Miles")
is_equal_to = Label(text="is equal to")
km_converted_value = Label(text="0.0")
km_indicator = Label(text="KM")


def convert_to_km():
    value_in_miles = float(input.get() or 0)
    result = value_in_miles * 1.609
    km_converted_value.config(text=f"{result}")


button = Button(text="calculate", command=convert_to_km)


input.grid(row=0, column=1, padx=2, pady=1)
miles_indicator.grid(row=0, column=2, padx=2, pady=1)
is_equal_to.grid(row=1, column=0, padx=2, pady=1)
km_converted_value.grid(row=1, column=1, padx=2, pady=1)
km_indicator.grid(row=1, column=2, padx=2, pady=1)
button.grid(row=2, column=1, padx=2, pady=1)


root.mainloop()
