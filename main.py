from tkinter import *

window = Tk()
window.title("Distance converter")
window.minsize(width=400, height=150)
window.eval("tk::PlaceWindow . center")
window.config(padx=50, pady=20)


def convert():
    miles_value = user_input.get()
    if miles_value.replace(".", "").isnumeric():
        kilometers = float(miles_value) * 1.609
        converted_amount.config(text=kilometers)
        error_message.config(text="")
    else:
        error_message.config(text="Please enter a number")


# Add placeholder text later
user_input = Entry(width=10)
user_input.grid(column=1, row=0)
user_input.insert(0, "Enter # of miles")
user_input.focus()

convert_from = Label(text="Miles")
convert_from.grid(column=2, row=0)
convert_from.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10, pady=10)

converted_amount = Label(text=0)
converted_amount.grid(column=1, row=1)
converted_amount.config(padx=10, pady=10)

convert_to = Label(text="Km")
convert_to.grid(column=2, row=1)
convert_to.config(padx=10, pady=10)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

error_message = Label()
error_message.grid(column=1, row=4)
error_message.config(padx=5, pady=5)

window.mainloop()
