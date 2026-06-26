from tkinter import *

a =[]
def submit():
    #print(list_box.get(list_box.curselection()))


    # type 1
    # food=[]
    # for i in list_box.curselection():
    #     food.insert(i,list_box.get(i))
    
    # print("you booked:")
    # for i in food:
    #     print(i)



    # type 2
    for i in list_box.curselection():
        global a
        print(list_box.get(i)) 
        a.append(list_box.get(i))
    # window.destroy()
  
   
window =Tk()
list_box= Listbox(window,font = ("Ariel",20,"bold"),
                  bg = "yellow",
                  width=15,
                  selectmode= MULTIPLE
                  )
list_box.insert(0,"Mazda")
list_box.insert(1,"Ford")
list_box.insert(2,"Nissan")
list_box.insert(3,"Benz")
list_box.insert(4,"Chevy")

list_box.config(height=list_box.size())

list_box.pack()


button =Button(window,
               text="Submit",
               font=(10),
               command=submit)

button.pack()



window.mainloop()
print(a)
unique_ordered_list = []

for item in a:
    if item not in unique_ordered_list:
        unique_ordered_list.append(item)
print(unique_ordered_list)
# unique_list = list(set(a))
# print(unique_list)

