from tkinter import *
import time 
from Ball import *

WIDTH=1080
HEIGHT=720



window =Tk()
window.geometry("1080x720")





imageufo=PhotoImage(file="tzz.png")
canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="black")

canvas.pack()

volly=Ball(canvas,0,0,100,20,30,"white")

bas=Ball(canvas,100,100,50,10,10,"Red")

while True:
    volly.move(WIDTH,HEIGHT)
    bas.move(WIDTH,HEIGHT)
    window.update()
    time.sleep(0.05)



window.mainloop()
# xvelocity=50
# yvelocity=30
    
#     label.place(x=label.winfo_x(),y=label.winfo_y()+50)

# ufo=canvas.create_image(0,0,image=imageufo,anchor=NW)
# ball=canvas.create_oval(100,100,200,200,fill="light blue")


# image_width=imageufo.width()
# image_height=imageufo.height()
# window.bind("<w>",moveup)
 
# while True:
#     imgcoord=canvas.coords(ufo)
#     if(imgcoord[0]>(WIDTH-image_width)) or(imgcoord[0]<0):
#         xvelocity=-xvelocity
#     if(imgcoord[1]>(HEIGHT-image_height)) or(imgcoord[1]<0):
#         yvelocity=-yvelocity


# while True:
#     canvas.move(ball,xvelocity,yvelocity)
#     imgcoord=canvas.coords(ball)
#     print(imgcoord)
#     if(imgcoord[0]>1000)or(imgcoord[0]<0):
#         xvelocity=-xvelocity
#     if(imgcoord[1]>720) or(imgcoord[1]<0):
#         yvelocity=-yvelocity