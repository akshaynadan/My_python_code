from tkinter import *
from tkinter import filedialog

def click():
    filepath = filedialog.asksaveasfilename()
    file= open(filepath,"r")
    print(file.read())
    file.close()

    

window =Tk()

button = Button(text= "Click",
                font=(10),
                command=click)
button.pack()


window.mainloop()