#imports
from tabnanny import check
from tkinter import *

#varibles
rowcount=0
columncount=0
namesList=[]

#building root()
root = Tk()
root.title("Sudoku")
root.geometry("500x500")

#Building Names List
"""for i in range(81):
    i.append(namesList)
    i = [str(j) for j in i]
print(namesList)"""

#functions


#widgets
outputText = StringVar([])    #StringVar() is a var used in widget 

#frames
sudokuFrame = Frame(root,width=500,height=200,bg="grey")
sudokuFrame.pack()
buttonFrame = Frame(root,width=500,height=200,bg="grey")
buttonFrame.pack()

#main frame buttons
checkBTN = Button(buttonFrame,text="Check",fg="black",width=59,height=3,justify=LEFT,bd=0,bg="#fff")
checkBTN.grid(row=9,column=9,columnspan=9,padx=1,pady=1)

#input fields
for j in range(9):
    rowcount=0
    for i in range(9):
        input = Entry(sudokuFrame,bd=0,justify=CENTER,width=7,textvariable=outputText).grid(row=rowcount,column=columncount,columnspan=9,padx=1,pady=1,ipady=13)
        rowcount+=1
        columncount+=1

root.mainloop()