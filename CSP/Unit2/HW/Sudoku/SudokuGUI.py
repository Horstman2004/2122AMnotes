#imports
from tkinter import *

#varibles
rowcount=0
columncount=0
numList=[]
finalList=[]
finalFinalList=[]
#building root()
root = Tk()
root.title("Sudoku Checker")
root.geometry("500x500")

#Building Names List (Scrapped)
"""
for i in range(81):
    i.append(namesList)
    i = [str(j) for j in i]
print(namesList)
"""

#functions
def get():
    global numList,finalList
    index1=0
    index2=9
    for i in numList:   
        print(i.get())
        finalList.append(i.get())   
    for l in range(9):              #Combining single strings into 9 string with 9 numbers
        for k in range(1):          #Joins the strings
            k=finalList[index1:index2]
            k = ''.join(map(str, k))
            finalFinalList.append(k)
            index1+=9               #Adds to index1 & 2 to get next group of strings
            index2+=9         
    print(finalList)
    horizontalCheck(finalList)      #Sending list ot first check


def rowChecker(rowToCheck):
    global rowLabel,failedText
    temp=[]
    print(rowToCheck)
    for i in range(len(rowToCheck)):        #loops through list to find errors
        if rowToCheck[i] in temp:
            print(f"Failed at {i+1}")
            failedText.set(f"Failed at Column: {i+1}. Keep Rechecking...")  #Notifies User of Error
            return False
        else:           #If no errors returns "Sudoku is Correct"
            temp.append(rowToCheck[i])
            failedText.set("Sudoku is Correct")

def horizontalCheck(boardToCheck):  
    for i in range(len(numList)):   
        rowChecker(boardToCheck[i])
        
#frames
sudokuFrame = Frame(root,width=500,height=200,bg="grey")
sudokuFrame.pack()
buttonFrame = Frame(root,width=500,height=200,bg="grey")
buttonFrame.pack()

#main frame buttons & labels
failedText = StringVar()
colLabel = Label(buttonFrame,textvariable=failedText,fg="black",width=30,height=3,justify=LEFT,bd=0,bg="#fff").grid(row=1,column=1,columnspan=1)
rowLabel = Label(buttonFrame,textvariable=failedText,fg="black",width=30,height=3,justify=LEFT,bd=0,bg="#fff").grid(row=1,column=2,columnspan=2)
checkBTN = Button(buttonFrame,text="Sudoku Checker",fg="black",width=59,height=3,justify=LEFT,bd=0,bg="#fff",command=lambda:get()).grid(row=2,column=1,columnspan=9,padx=1,pady=1)


#building input fields
for j in range(9):
    rowcount=0
    for i in range(9):
        outputText = StringVar()
        input = Entry(sudokuFrame,bd=0,justify=CENTER,width=7,textvariable=outputText)
        input.grid(row=j,column=i,padx=2,pady=2,ipady=13)
        numList.append(input)
        rowcount+=1
        columncount+=1
root.mainloop()