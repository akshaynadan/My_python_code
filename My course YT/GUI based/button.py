from tkinter import *

def click():
    print("Got Details")


window = Tk()

button = Button(window,
                text="Press Here",
                command=click,
                font=("Comic Sans",30),
                fg="blue",
                bg="black",
                activeforeground="blue",
                activebackground="black"
                
                )
button.pack()


window.mainloop()