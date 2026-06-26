from tkinter import *

def checked():
    print("Agree" if x.get() else "Disagree")




window = Tk()

x=IntVar()
check_button = Checkbutton(window,text="I agreee to the Conditions",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=checked)
check_button.pack(side=BOTTOM)





window.mainloop()