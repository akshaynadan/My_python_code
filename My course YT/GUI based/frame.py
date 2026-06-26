from tkinter import *

window= Tk()

window.title("New App name")
window.geometry("1080x720")
window.config(background="White")
logo = PhotoImage(file="tt.png")
window.iconphoto(True,logo)

frame = Frame(window)
frame.pack()
Button(frame,text="W",font=("consolas",20),width=3).pack(side="top")
Button(frame,text="A",font=("consolas",20),width=3).pack(side="left")
Button(frame,text="S",font=("consolas",20),width=3).pack(side="left")
Button(frame,text="D",font=("consolas",20),width=3).pack(side="left")




window.mainloop()