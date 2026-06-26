from tkinter import *
from tkinter import messagebox

def click():
    if messagebox.askquestion(title = "first msg",
                        message="your info"):
        print("yu selcet yes")
    else:
        print("yu selseted no")

window = Tk()

button = Button(window,font=(10),text="click me",
                command=click,
)

button.pack()
window.mainloop()
