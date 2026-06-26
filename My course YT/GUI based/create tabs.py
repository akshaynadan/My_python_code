from tkinter import *
from tkinter import ttk



window = Tk()

window.title("New App name")
window.geometry("1080x720")
window.config(background="White")
logo = PhotoImage(file="tt.png")
window.iconphoto(True,logo)
notebook = ttk.Notebook(window,padding=30)
tab1=Frame(notebook)
tab2=Frame(notebook)
tab3=Frame(notebook)


case= notebook.add(tab1,text=" Tab 1     ")
notebook.add(tab2,text=" Tab 2")

notebook.pack(expand=True,fill="both")



Label(tab1,text="Hello Good Morning").pack(padx=100,pady=250)
Label(tab2,text="Sorry to let yu go").pack()

# tab1=Frame()
# tab2=Frame()









window.mainloop()