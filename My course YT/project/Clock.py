from tkinter import *
from time import *


def update():
    timestring=strftime("%I:%M:%S %p")
    timelabel.config(text=timestring)
   
    
    daystring=strftime("%A")
    daylabel.config(text=daystring)


    datestring=strftime("%d-%B-%Y")
    datelabel.config(text=datestring)

    window.after(1000,update)
   


window = Tk()
icon =PhotoImage(file="ttt.png")
nn =PhotoImage(file="mm.PNG")
window.title("New Window")
window.iconphoto(True,nn)

datelabel=Label(window,
                bg="Black",
                text="Time",
                font=("Emerlad",20,"bold"),
                relief=RAISED,
                bd=10,
                fg="White",
                # height=5,
                width=40
                )

datelabel.pack()
daylabel=Label(window,
                bg="Black",
                font=("Emerlad",20,"bold"),
                relief=RAISED,
                bd=10,
                fg="White",
                # height=2,
                width=40
)

daylabel.pack()
timelabel=Label(window,
                bg="Black",
                text="Time",
                font=("Emerlad",20,"bold"),
                relief=RAISED,
                bd=10,
                fg="White",
                height=5,
                width=40
                )
timelabel.pack()








update()





window.mainloop()