from tkinter import *


window = Tk()

firstname=Label(window,text="First Name : ",bg ="red",).grid(row=0,column=0)
fnentry=Entry(window).grid(row=0,column=1)

lastname=Label(window,text="Last Name : ",bg ="blue").grid(row=2,column=0)
lnentry=Entry(window).grid(row=2,column=1)

email=Label(window,text="E-mail : ",bg ="yellow").grid(row=4,column=0)
eentry=Entry(window).grid(row=4,column=1)

submit =Button(window,text="Submit",
               font=(8)).grid(row=5,column=0,columnspan=2)

window.mainloop()