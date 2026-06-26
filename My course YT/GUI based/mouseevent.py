from tkinter import *

def dosomething(event):
    print("you did a thing "+str(event.x),str(event.y))


window = Tk()
# window.bind("<Button-1>",dosomething)
# window.bind("<Button-2>",dosomething)
# window.bind("<Button-3>",dosomething)
window.bind("<Enter>",dosomething) # there is Enter leave motion




window.mainloop()