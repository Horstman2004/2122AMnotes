#imports
from tkinter import *

#varibles
rowcount=0
columncount=0
numList=[]
finalList=[]
#building root()
root = Tk()
root.title("Sudoku Checker")
root.geometry("500x500")

#Building Names List
"""
for i in range(81):
    i.append(namesList)
    i = [str(j) for j in i]
print(namesList)
"""

#functions
def get():
    global numList,finalList
    index1=1
    index2=9
    for i in numList:
        print(i.get())
        finalList.append(i.get())
        for k in range(1):
            tempList=[]
            k=finalList[index1:index2]
            tempList.append(k)
            index1+=9
            index2+=9
            print(tempList)
            
            
                
                
    print(finalList)
        
def rowChecker(rowToCheck):
    temp=[]
    print(rowToCheck)
    for i in range(len(rowToCheck)):
        if rowToCheck[i] in temp:
            print(f"Failed at {i+1}")
            print(temp)
            return False
        else:
            temp.append(rowToCheck[i])

def horizontalCheck(boardToCheck):
    for i in range(len(numList)):
        rowChecker(boardToCheck[i])
        
#frames
sudokuFrame = Frame(root,width=500,height=200,bg="grey")
sudokuFrame.pack()
buttonFrame = Frame(root,width=500,height=200,bg="grey")
buttonFrame.pack()

#main frame buttons & labels
checkBTN = Button(buttonFrame,text="Sudoku Checker",fg="black",width=59,height=3,justify=LEFT,bd=0,bg="#fff",command=lambda:get()).grid(row=9,column=9,columnspan=9,padx=1,pady=1)


#input fields
for j in range(9):
    rowcount=0
    for i in range(9):
        outputText = StringVar()
        input = Entry(sudokuFrame,bd=0,justify=CENTER,width=7,textvariable=outputText)
        input.grid(row=rowcount,column=columncount,columnspan=9,padx=2,pady=2,ipady=13)
        numList.append(input)
        rowcount+=1
        columncount+=1



root.mainloop()