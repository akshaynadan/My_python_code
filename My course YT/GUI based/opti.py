from tkinter import *

selected_items = []  # Global list to store selections

def submit():
    global selected_items
    selected_items = [list_box.get(i) for i in list_box.curselection()]
    
    # Remove duplicates while preserving order
    selected_items = list(dict.fromkeys(selected_items))

    print("You booked:", selected_items)
    
    # Uncomment to close window after selection
    window.destroy()  



def drag_start(event):
    widget=event.widget
    widget.startx=event.x
    widget.starty=event.y

def motion(event):
    widget=event.widget
    X=widget.winfo_x()-widget.startx+event.x
    Y=widget.winfo_y()-widget.starty+event.y
    widget.place(x=X,y=Y)


window = Tk()
# program 1

list_box = Listbox(
    window, font=("Arial", 20, "bold"),
    bg="yellow", width=15,
    selectmode=MULTIPLE
)
# cars = ["Mazda", "Ford", "Nissan", "Benz", "Chevy"]
# for i, car in enumerate(cars):
#     list_box.insert(i, car)

# list_box.config(height=list_box.size())
# list_box.pack()

# Button(window, text="Submit", font=(10), command=submit).pack()



# print(selected_items)  # Print outside Tkinter loop


# program 2

# label =Label(window,bg="light blue",height=10,width=10)
# label.place(x=0,y=0)


# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",motion)



# program 3





window.mainloop()
