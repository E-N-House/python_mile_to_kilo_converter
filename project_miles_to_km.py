from tkinter import *


# conversion function
def start_calculation():
    # obtain user input validates this is a number
    try:
        miles = float(miles_input.get())
        result = round(1.609*miles, 2)
        calculation.config(text=result)
    except(ValueError):
        # clears entry and replaces with prompt enter a number
        miles_input.delete(0,END)
        miles_input.insert(END, "Enter A Number")


# create layout
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=10, pady=10)
window.minsize(width=200, height=100)

miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

info_label = Label(text="is equal to ")
info_label.grid(column=0, row=1)

calculation = Label(text=0)
calculation.grid(column=1, row=1)

kms_label = Label(text="Km")
kms_label.grid(column=2, row=1)
kms_label.config(pady=10)

calc_button = Button(text="Calculate")
calc_button.grid(column=1, row=2)
calc_button.config(command=start_calculation)

window.mainloop()
