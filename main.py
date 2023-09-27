from functools import partial
from tkinter import *

window = Tk()
window.title("Distance converter")
window.minsize(width=400, height=150)
window.eval("tk::PlaceWindow . center")
window.config(padx=50, pady=20)


def convert():
    if (user_input.get()).replace(".", "").isnumeric():
        if convert_from['text'] == "Miles":
            kilometers = float(user_input.get()) * 1.609
            converted_amount.config(text=kilometers)
            error_message.config(text="")
        elif convert_from['text'] == "Km":
            miles = float(user_input.get()) / 1.609
            converted_amount.config(text=miles)
            error_message.config(text="")
    else:
        error_message.config(text="Please enter a number")


def switch_modes(starting_unit):
    # imperial_to_metric = True
    # starting_unit = radio_state.get()
    if starting_unit == "Miles":
        convert_from.config(text="Miles")
        convert_to.config(text="Km")
        # imperial_to_metric = True
    elif starting_unit == "Kilometers":
        convert_from.config(text="Km")
        convert_to.config(text="Miles")
        # imperial_to_metric = False
    # return imperial_to_metric


def button_test():
    print(f"You clicked a button" + radio_state.get())


# Add placeholder text later
user_input = Entry(width=10)
user_input.grid(column=1, row=1)
user_input.insert(0, "Enter # of miles")
user_input.focus()

convert_from = Label(text="Miles")
convert_from.grid(column=2, row=1)
convert_from.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=2)
is_equal_to.config(padx=10, pady=10)

converted_amount = Label(text=0)
converted_amount.grid(column=1, row=2)
converted_amount.config(padx=10, pady=10)

convert_to = Label(text="Km")
convert_to.grid(column=2, row=2)
convert_to.config(padx=10, pady=10)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=3)

error_message = Label()
error_message.grid(column=1, row=5)
error_message.config(padx=5, pady=5)

radio_state = StringVar()
miles_to_km = Radiobutton(text="Miles to KM", value="Miles", variable=radio_state, command=partial(switch_modes, "Miles"))
miles_to_km.grid(column=0, row=0)

km_to_miles = Radiobutton(text="KM to miles", value="Kilometers", variable=radio_state, command=partial(switch_modes, "Kilometers"))
km_to_miles.grid(column=2, row=0)

window.mainloop()