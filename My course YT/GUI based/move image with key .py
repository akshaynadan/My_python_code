from tkinter import *

 
def wkey(event):
    # widget=event.widget
    # widget.startx=event.x
    # widget.startx=event.x
   label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def akey(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def skey(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def dkey(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())


window = Tk()

window.geometry("1080x720")



image = PhotoImage(file="ttt.png")
label=Label(window,image=image,bg="light blue")
label.place(x=100,y=100)

window.bind("<w>",wkey)
window.bind("<a>",akey)
window.bind("<s>",skey)
window.bind("<d>",dkey)



window.mainloop()