from tkinter import *

def openfile():
    print("Got Details")
def savefile():
    print("Got Saved")
def copy():
    print("file Copied")
def cut():
    print("Got cut")


window = Tk()
menubar= Menu(window)
window.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)
editmenu=Menu(menubar)
menubar.add_cascade(label="file",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Exit",command=quit)
editmenu.add_checkbutton(label="copy",command=copy)
editmenu.add_separator()
editmenu.add_radiobutton(label="cut",command=cut)
editmenu.add_command(label="paste")
# menubar1.add_cascade(label="Edit")

# filemenu.add_command(label="File")


window.mainloop()