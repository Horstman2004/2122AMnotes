from tkinter import *


root = Tk()
root.title("tk")
root.geometry("400x400")

mainFrame = Frame(root,bg="white",width=400,height=400)
mainFrame.grid(column=4,row=4)
mainFrame.pack()

blueFrame = Frame(mainFrame,bg="blue",width=300,height=200)
blueFrame.grid(row=0,column=0)

greenFrame = Frame(mainFrame,bg="green",width=100,height=200)
greenFrame.grid(row=0,column=1)

redFrame = Frame(mainFrame,bg="red",width=300,height=200)
redFrame.grid(row=1,column=0)

yellowFrame = Frame(mainFrame,bg="yellow",width=100,height=200)
yellowFrame.grid(row=1,column=1)


root.mainloop()