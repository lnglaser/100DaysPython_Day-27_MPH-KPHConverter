from tkinter import *

window = Tk()
window.title("Distance converter")
window.minsize(width=400, height=200)
window.eval("tk::PlaceWindow . center")
window.config(padx=20, pady=20)


def convert():
    kilometers = float(user_input.get()) * 1.609
    converted_amount.config(text=kilometers)


# Add placeholder text later
user_input = Entry(width=5)
user_input.grid(column=1, row=0)

convert_from = Label(text="Miles")
convert_from.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

converted_amount = Label(text=0)
converted_amount.grid(column=1, row=1)

convert_to = Label(text="Km")
convert_to.grid(column=2, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)


window.mainloop()
