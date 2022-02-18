#Imports
from tkinter import *
from turtle import numinput

#Global Varibles
expression=""
operator=0
#Bulid out root
root = Tk()
root.title("Calulator")
root.geometry("312x324")

#Functions
def buttonClick(item):
    global expression,operator
    expression += str(item)
    print(expression)
    outputText.set(expression)
    if operator < 1:
        if expression == "+" or "/" or "*" or "-":
            operator+1
        else:
            expression="ERROR"

def clearButton():
    global expression
    expression=""
    print(expression)
    outputText.set(expression)
    
def equalButton():
    global expression,operator
    if "/0" in expression:
        result="ERROR"
    result=str(eval(expression))
    expression=""
    print(result)
    outputText.set(result)
    operator+=0
    
        
    
outputText = StringVar()    #StringVar() is a var used in widget 
                            #if you're wanting to pass a value to a widget, you need a StringVar()

#Widgets
inputFrame = Frame(root,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
inputFrame.pack(side=TOP)           #will make sure it stays at the top

inputField = Entry(inputFrame,bd=0,justify=RIGHT,width=312,textvariable=outputText)
inputField.grid(row=0,column=0)
inputField.pack(ipady = 10)       #ipady i internal padding

buttonFrame = Frame(root,width=312,height=272.5,bg="grey")
buttonFrame.pack()

clear = Button(buttonFrame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",command=lambda:clearButton())
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

divide = Button(buttonFrame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("/"))
divide.grid(row=0,column=3,columnspan=3,padx=1,pady=1)

seven = Button(buttonFrame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(7)).grid(row=1,column=0,padx=1,pady=1)
eight = Button(buttonFrame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(8)).grid(row=1,column=1,padx=1,pady=1)
nine = Button(buttonFrame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(9)).grid(row=1,column=2,padx=1,pady=1)
multiply = Button(buttonFrame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("*")).grid(row=1,column=3,padx=1,pady=1)

#third row
four = Button(buttonFrame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(4)).grid(row=2,column=0,padx=1,pady=1)
five = Button(buttonFrame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(5)).grid(row=2,column=1,padx=1,pady=1)
six = Button(buttonFrame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(6)).grid(row=2,column=2,padx=1,pady=1)
minus = Button(buttonFrame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("-")).grid(row=2,column=3,padx=1,pady=1)

#fourth row
one = Button(buttonFrame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(1)).grid(row=3,column=0,padx=1,pady=1)
two = Button(buttonFrame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(2)).grid(row=3,column=1,padx=1,pady=1)
three= Button(buttonFrame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(3)).grid(row=3,column=2,padx=1,pady=1)   
plus = Button(buttonFrame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("+")).grid(row=3,column=3,padx=1,pady=1)

#fifth row
zero = Button(buttonFrame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff",command=lambda:buttonClick(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
dot = Button(buttonFrame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick(".")).grid(row=4,column=2,padx=1,pady=1)
equals = Button(buttonFrame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:equalButton()).grid(row=4,column=3,padx=1,pady=1)


root.mainloop()