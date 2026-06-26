from tkinter import*
from tkinter import font

window = Tk()
# lis =list(font.families())
icon =PhotoImage(file="ttt.png")
nn =PhotoImage(file="mm.PNG")
window.title("New Window")
window.iconphoto(True,nn)
label = Label(window,
              text="Testing Labels !",
              font=('Emerald Beacon',40,"italic"),
              fg="blue",
              bg="white",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=10,
              image=icon,
              compound="top")
label.pack()
# label.place(x=100,y=0)
# print(lis)


window.mainloop()