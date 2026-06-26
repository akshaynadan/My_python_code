from tkinter import *


def user_details():
    user = entry_username.get()
    print("Username :"+user)

    passw = entry_password.get()
    print("Password :"+passw)
    entry_username.config(state=DISABLED)
    entry_password.config(state=DISABLED)


def retry():
    entry_username.delete(0,END)
    entry_password.delete(0,END)





window = Tk()

window.title("New App name")
window.geometry("1080x720")
window.config(background="White")
logo = PhotoImage(file="tt.png")
window.iconphoto(True,logo)

label= Label(window,text="Type your User Name",
             font=("Arial",20,"bold"),
             fg="black",
             bg="white",
             )

label.place(x=0,y=0)

entry_username =Entry(window,font=("Times New Roman",16),
                      fg="black",
                      bg="white",
                      )
entry_username.place(x=20,y=40)

label= Label(window,text="Type your Password",
             font=("Arial",20,"bold"),
             fg="black",
             bg="white")

label.place(x=0,y=80)
entry_password =Entry(window,font=("Times New Roman",16),
                      fg="black",
                      bg="white",
                      show="*"
                      )
entry_password.place(x=20,y=120)


button = Button(window,text="Submit",
                font=("bold"),
                fg="black",
                bg="white",
                bd=4,
                command=user_details)
button.place(x=20,y=160)

button_2= Button(window,text="Retry",
                font=("bold"),
                fg="black",
                bg="white",
                bd=4,
                command=retry)
button_2.place(x=150,y=160)

window.mainloop()