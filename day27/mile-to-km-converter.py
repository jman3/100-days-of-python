from tkinter import *


def convert():
    miles_input = input.get()
    km = round(float(miles_input) * 1.609, 1)
    converted_km.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=30, pady=30)

# Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

converted_km = Label(text="0")
converted_km.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
input.insert(END, "0")
input.grid(column=1, row=0)

window.mainloop()
