#imports
from tkinter import *

#building root()
root = Tk()
root.title("NumberConverter")
root.geometry("355x460")

#functions
def binButton(decimal):
    #1st find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=2**exp:
        digitList.insert(0,2**exp) #change the exponent to change the base
        exp+=1
    print(digitList)

    #2nd we itterated through the bits to find how many of eac bit is in our number
    for i in range(len(digitList)):
        if decimal >= digitList[i]:
            decimal-=digitList[i]
            digitList[i] = "1"
        else:
            digitList[i] = "0"
        digitList = [int(item) for item in digitList]
    print(digitList)
    
def octButton(decimal):
    digitList=[]
    exp = 0
    while decimal>=8**exp:
        digitList.insert(0,8**exp) #change the exponent to change the base
        exp+=1
    print(digitList)
    
    for i in range(len(digitList)):
        if decimal >= digitList[i]:
            decimal-=digitList[i]
        digitList = [int(item) for item in digitList]

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
    result=(str(out))
    print(result)
    outputText.set(result)

def quitButton():
    mainFrame.quit()

#auto conversion function
def toDecimal(base,digit):
    digitList = list(digit)
    outputNum = 0
    conversionList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for exp, digit in enumerate(digitList[-1::-1]):
        conversionDigit = conversionList.index(digit)
        if int(conversionDigit)/base >= 1:
            print('Error')
            break
        outputNum = (int(conversionDigit) * (base**exp)) + outputNum
    print(outputNum)

#widgets
outputText = StringVar()    #StringVar() is a var used in widget 

#frames
mainFrame = Frame(root,width=350,height=400,bg="grey")
mainFrame.pack()

#input fields
inputField = Entry(mainFrame,bd=0,justify=RIGHT,width=59,textvariable=outputText)
inputField.insert(0,'Enter Decimal Number')
inputField.grid(row=0,column=0,columnspan=3,padx=1,pady=1,ipady=10)

baseInput = Entry(mainFrame,bd=0,justify=RIGHT,width=59,textvariable=outputText)
baseInput.grid(row=1,column=0,columnspan=3,padx=1,pady=1,ipady=10)
baseInput.insert(0, 'Enter Base for Number Conversion')

#instruction labels
step1LBL = Label(mainFrame,text="Username: ")

#conversion buttons
dec = Button(mainFrame,text="Decimal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:toDecimal(baseInput,inputField)).grid(row=2,column=0,padx=1,pady=1)
bin = Button(mainFrame,text="Binary",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:binButton(inputField)).grid(row=3,column=0,padx=1,pady=1)
oct = Button(mainFrame,text="Octal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:octButton()).grid(row=4,column=0,padx=1,pady=1)
hex = Button(mainFrame,text="Hexdecimal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:hexButton(inputField)).grid(row=5,column=0,padx=1,pady=1)
quit = Button(mainFrame,text="Quit",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:quitButton()).grid(row=6,column=0,padx=1,pady=1)


root.mainloop()