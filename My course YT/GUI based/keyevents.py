from tkinter import *

def func(event):
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",func)
label=Label(window,font=("Ariel",50))
label.pack()

window.mainloop()