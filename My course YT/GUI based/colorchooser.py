from tkinter import *
from tkinter import colorchooser
def click():
    window.config(bg=colorchooser.askcolor()[1])
    # print(color)
    # print(hexa:=color[1])
    # window.config(bg=color[1 ])


window =Tk()

window.geometry("1080x720")
button=Button(window,text="Click me",
              command=click)
button.pack()

window.mainloop()