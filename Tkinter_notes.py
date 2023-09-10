import tkinter
# create a window like screen in turtle
window = tkinter.Tk()
# REMEMBER to tell window to enter a built-in while loop to have it show on screen at END of file
# window.mainloop()

# set title
window.title("Title goes here!")

# resize screen on appearing by default it will scale to fit everything you tell it to
# but if you want it to be a particular size and there isn't a lot in there use .minsize()
window.minsize(width=600, height=400)

# initialize a label that will appear on screen
label_one = tkinter.Label(text="Label One", font=("Arial", 20, "bold"))
# .pack() will display component on screen and center it by default
# can also tell it expand=True and it will fit to fill
# label_one.pack(side="bottom") ===> this will set the component to appear at bottom of screen
label_one.grid(column=0, row=0)

# can update and change propreties later on via dict key access
label_one["bg"] = "red"

# can also update multiple with .config method
label_one.config(text= "channgggess", background="blue")


# buttons
def button_click():
    print("clicked")
    input_text = my_input.get()
    print(input_text)
    if label_one["text"] == "Button Was Clicked":
        label_one.config(text="click again", background="green")
    else:
        label_one.config(text=input_text, background="light blue")


# command= takes in a function WITHOUT () and will activate on button press
my_button = tkinter.Button(text="Button", command=button_click)
# don't forget .pack to get it to appear on screen
my_button.grid(column=1, row=1)

# Entry similiar to input will allow for user prompt
my_input = tkinter.Entry(width=20)
my_input.grid(column=3, row=2)

newer_button = tkinter.Button(text="new button")
newer_button.grid(column=2, row=0)

# can also use Canvas to layer items on top of each other
# highlightthickness will create or remove the line around the border of canvas bounds
canvas = tkinter.Canvas(width=220, height=224, background="blue", highlightthickness=0)
# to add an image in must make an object called PhotoImage to store the filepath in
image_img = tkinter.PhotoImage(file="image.png")

# numbers are x and y of pixels kind of have to eyeball it in tkinter based on knowing your image's dimensions
# then take the above object and have image=image_object
canvas.create_image(110, 112, image=image_img)

# to add a text on it need to also eyeball where to plac x and y, fill= text color
canvas.create_text(110, 140, text="00:00", fill="white")
window.mainloop()
