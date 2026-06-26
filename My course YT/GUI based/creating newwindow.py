from tkinter import *

def createwindow():
    newwindow=Tk()
    window.destroy()

window = Tk()

window.title("New App name")
window.geometry("1080x720")
window.config(background="White")
logo = PhotoImage(file="tt.png")
window.iconphoto(True,logo)


Button(window,
              text="Go to New Window",
              command=createwindow).pack()
window.mainloop()
