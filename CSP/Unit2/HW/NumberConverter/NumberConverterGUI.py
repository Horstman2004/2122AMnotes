#imports
from tkinter import *

#building root()
root = Tk()
root.title("NumberConverter")
root.geometry("360x499")

#functions
def binButton(decimal):
    #find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=2**exp:
        digitList.insert(0,2**exp) #change the exponent to change the base
        exp+=1
    print(digitList)

    #itterate through the bits to find how many of each bit is in our number
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
    
    #conversion math from decimal to octal
    for i in range(len(digitList)):
        if decimal >= digitList[i]:
            decimal-=digitList[i]
        digitList = [int(item) for item in digitList]
        
    #configuring the digitList to a string to be printed
    out=" "
    for b in digitList:
        out+=str(b)
    result=(str(out))
    print(result)
    outputText.set(result)

def hexButton(decimal):
    #find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=16**exp:
        digitList.insert(0,16**exp) #change the exponent to change the base
        exp+=1
    print(digitList)
    
    #itterated through the bits to find how many of eac bit is in our number
    for i in range(len(digitList)):
        temp=digitList[i]
        digitList[i]=decimal//digitList[i]
        decimal-=(digitList[i]*temp)
    #concatenated 1's and 0's to output our string
    #Concate the digitList together
    
    #configuring the digitList to a string to be printed
    out=" "
    for b in digitList:
        out+=str(b)
    result=(str(out))
    print(result)
    outputText.set(result)

def quitButton():
    mainFrame.quit()

#auto conversion function
def toDecimal(base,digit):
    #conversion for any base and digit to be converted to decimal
    digitList = list(digit)
    outputNum = 0
    
    #list for conversions up to base 16
    conversionList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    #itterating through the digit index by index to convert whatever base to a decimal
    for exp, digit in enumerate(digitList[-1::-1]):         #enumeratue yields single indexs at a time to be converted 
        conversionDigit = conversionList.index(digit)
        if int(conversionDigit)/base >= 1:
            print('Error')
            break
        outputNum = (int(conversionDigit) * (base**exp)) + outputNum
    print(outputNum)
    
    #configuring the digitList to a string to be printed
    out=" "
    for b in outputNum:
        out+=str(b)
    result=(str(out))
    print(result)
    outputText.set(result)

#widgets
outputText = StringVar()    #StringVar() is a var used in widget 
outputText2 = StringVar()

#frames
mainFrame = Frame(root,width=350,height=400,bg="grey")
mainFrame.pack()

#input fields
inputField = Entry(mainFrame,bd=0,justify=RIGHT,width=59,textvariable=outputText)
inputField.insert(0,'Enter Decimal Number')
inputField.grid(row=0,column=0,columnspan=3,padx=1,pady=1,ipady=10)

baseInput = Entry(mainFrame,bd=0,justify=RIGHT,width=59,textvariable=outputText2)
baseInput.insert(0, 'Enter Base for Number Conversion')
baseInput.grid(row=1,column=0,columnspan=3,padx=1,pady=1,ipady=10)

#instruction labels
step1LBL = Label(mainFrame,text="Username: ")

#conversion buttons
dec = Button(mainFrame,text="Convert",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:toDecimal(baseInput,inputField)).grid(row=2,column=0,padx=1,pady=1)
bin = Button(mainFrame,text="Binary",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:binButton(inputField)).grid(row=3,column=0,padx=1,pady=1)
oct = Button(mainFrame,text="Octal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:octButton()).grid(row=4,column=0,padx=1,pady=1)
hex = Button(mainFrame,text="Hexdecimal",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:hexButton(inputField)).grid(row=5,column=0,padx=1,pady=1)
quit = Button(mainFrame,text="Quit",fg="black",width=50,height=5,bd=0,bg="#fff",command=lambda:quitButton()).grid(row=6,column=0,padx=1,pady=1)


root.mainloop()