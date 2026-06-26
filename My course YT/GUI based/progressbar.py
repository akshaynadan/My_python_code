from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB= 100
    download=0
    speed =1
    while (download<GB):
        time.sleep(0.05) 
        bar["value"]+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        tsk.set("("+str(download)+"/"+str(GB)+") Completed")
        window.update_idletasks()
    
        
    

window = Tk()
percent =StringVar()
tsk=StringVar()

bar= Progressbar(window,length=500)
bar.pack(padx=10,pady=20)
label=Label(window,textvariable=percent).pack()
tlabel=Label(window,textvariable=tsk).pack()
button=Button(window,text="Click Me",command = start).pack()




window.mainloop()
