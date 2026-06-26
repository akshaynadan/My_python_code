from tkinter import *

def click():
    print(input:=text.get("1.0",END))
  
    # window.destroy()
 
window = Tk()
text = Text(window,
            font=("Ink Free",15),
            bg="light yellow",
            padx=20,
            pady=20
            
)
text.pack()
button=Button(window,text="Submit",
              font=(10),
              command=click)
button.pack()
window.mainloop()