#python3 uses tkinter / python2 uses tkinter
from tkinter import *

#in turtle: wn=Screen()
root = Tk()                 #creates your screen
root.title("Hello")         #set window title
root.wm_geometry("200x100") #size of the window

#object = Constructor(window,options)
myLabel = Label(root,text="Hello GUI")  

myLabel.pack()      # pack it into the screen THIS IS REQUIRED

root.mainloop()

#tutorialspoint
#geeksforgeeks