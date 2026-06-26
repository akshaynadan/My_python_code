from tkinter import *


window= Tk()

window.geometry("420x420")
window.title("My New Tab")
icon = PhotoImage(file="mm.png")
window.iconphoto(True,icon)
window.config(background="black")
icondis =PhotoImage(file="ttt.PNG")


def book():
    print("you booked Ford" if(x.get()==0) 
          else "you booked Nissan" if(x.get()==1) 
          else "you booked Toyota"if(x.get()==2) 
          else "you booked Benz" )
    
    
    
    
    
    # if(x.get()==0):
    #     print("you booked Ford")
    #     m=0
    #     while (len(lis))>m:
    #         lis[m].config(state = DISABLED)
    #         m+=1
    # elif(x.get()==1):
    #     print("you booked Nissan")
    #     m=0
    #     while (len(lis))>m:
    #         lis[m].config(state = DISABLED)
    #         m+=1
    # elif(x.get()==2):
    #     print("you booked Toyota")
    #     m=0
    #     while (len(lis))>m:
    #         lis[m].config(state = DISABLED)
    #         m+=1
    # else:
    #     print("you booked Benz")
    #     m=0
    #     while (len(lis))>m:
    #         lis[m].config(state = DISABLED)
    #         m+=1

    


# creating Radio butoon program
car =["Ford","Nissan","Toyoto","BenZ"]
x=IntVar()
lis=[]
for i in range(len(car)):
    radio_button=Radiobutton(window,text=car[i],
                             variable=x,
                             value=i,
                             padx=10,
                             pady=5,
                             image=icondis,
                             compound=RIGHT,
                             indicator=0,
                             width=400,
                             command=book

                            )
    radio_button.pack(anchor=W)
    lis.append(radio_button)






window.mainloop()
