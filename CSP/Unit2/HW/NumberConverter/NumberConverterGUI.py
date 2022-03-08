#imports
from tkinter import *

#varibles


#building root()
root = Tk()
root.title("NumberConverter")
root.geometry("355x460")

#functions
#def decButton():
    
#def binButton():
    
#def octButton():

def hexButton(decimal):
    #1st find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=16**exp:
        digitList.insert(0,16**exp) #change the exponent to change the base
        exp+=1
    print(digitList)

    #2nd we itterated through the bits to find how many of eac bit is in our number
    for i in range(len(digitList)):
        temp=digitList[i]
        digitList[i]=decimal//digitList[i]
        decimal-=(digitList[i]*temp)
    #3rd concatenated our 1's and 0's to output our string
    #4th Concate the digitList together
    out="0x"
    for b in digitList:
        out+=str(b)
    print(out)

def quitButton():
    mainFrame.quit()

#widgets
outputText = StringVar()    #StringVar() is a var used in widget 

#frames
mainFrame = Frame(root,width=350,height=400,bg="grey")
mainFrame.pack()

#input fields
inputField = Entry(mainFrame,bd=0,justify=RIGHT,width=59,textvariable=outputText)
inputField.grid(row=0,column=0,columnspan=3,padx=1,pady=1,ipady=10)

#main frame buttons
dec = Button(mainFrame,text="Decimal to Decimal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:decButton()).grid(row=1,column=0,padx=1,pady=1)
binary = Button(mainFrame,text="Decimal to Binary",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:binButton()).grid(row=2,column=0,padx=1,pady=1)
oct = Button(mainFrame,text="Decimal to Octal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:octButton()).grid(row=3,column=0,padx=1,pady=1)
hex = Button(mainFrame,text="Decimal to Hexdecimal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:hexButton(inputField)).grid(row=4,column=0,padx=1,pady=1)
quit = Button(mainFrame,text="Quit",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:quitButton()).grid(row=5,column=0,padx=1,pady=1)




root.mainloop()