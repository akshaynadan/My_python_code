from tkinter import*
import time


WIDTH=1080
HEIGHT=720
Xvelocity=30
Yvelocity=20

window=Tk()
canvas=Canvas(window,height=HEIGHT,width=WIDTH,bg="light blue")
canvas.pack()

myimage=PhotoImage(file="tttt.png")
image_canv=canvas.create_image(0,0,image=myimage,anchor=NW)

image_width=myimage.width()
image_height=myimage.height()


while True:
    cooridinatess =canvas.coords(image_canv)
    print(cooridinatess)
    if (cooridinatess[0]>=(WIDTH-image_width))or (cooridinatess[0]<0):
        Xvelocity=-Xvelocity
    if(cooridinatess[1]>=(HEIGHT-image_height))or (cooridinatess[1]<0):
        Yvelocity=-Yvelocity

    canvas.move(image_canv,Xvelocity,Yvelocity)
    window.update()
    time.sleep(0.08)


window.mainloop()