from tkinter import *

window = Tk()
window.title("Distance converter")
window.minsize(width=400, height=150)
window.eval("tk::PlaceWindow . center")
window.config(padx=50, pady=20)


def convert():
    if (user_input.get()).replace(".", "").isnumeric():
        kilometers = float(user_input.get()) * 1.609
        converted_amount.config(text=kilometers)
        error_message.config(text="")
    else:
        error_message.config(text="Please enter a number")


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

radio_state = IntVar()
miles_to_km = Radiobutton(text="Miles to KM")
miles_to_km.grid(column=0, row=0)

km_to_miles = Radiobutton(text="KM to miles")
km_to_miles.grid(column=2, row=0)

window.mainloop()
