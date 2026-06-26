from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_arc(50,50,500,500,fill="red",width=4,extent=180)
canvas.create_arc(50,50,500,500,fill="white",width=4,start=180,extent=180)
canvas.create_oval(200,200,330,330,fill="white",width=3)
canvas.create_oval(240,240,290,290,fill="black",width=3)
canvas.pack()



window.mainloop()