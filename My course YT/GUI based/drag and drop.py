from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX=event.x
    widget.startY=event.y

def drag_motion(event):
    widget = event.widget
    motionX=widget.winfo_x()-widget.startX+event.x
    motionY=widget.winfo_y()-widget.startY+event.y
    widget.place(x=motionX,y=motionY)



window = Tk()


label1= Label(window,bg="light blue",width=10,height=10)
label1.place(x=10,y=10)
label2= Label(window,bg="Pink",width=10,height=10)
label2.place(x=100,y=100)

label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_motion)
label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)




window.mainloop()