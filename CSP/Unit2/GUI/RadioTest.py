from tkinter import *

root = Tk()
root.geometry("200x100")

def selection():
    out = str(var.get())
    label.config(text=out)      #you reset a configuration

var = IntVar()





#at least 1 radio button is always marked
#if you want to have none selected, make sure to use checkboxes A.K.A Checkbuttons
r1 = Radiobutton(root,text="option 1",value=10,command=selection).pack()
r2 = Radiobutton(root,text="option 2",value=20,command=selection).pack()

outBTN = Button(root,text="click me",command=selection)
outBTN.pack()

label = Label(root).pack()

root.mainloop()