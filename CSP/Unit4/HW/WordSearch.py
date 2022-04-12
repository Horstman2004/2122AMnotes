#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Varibles


#User Interface
uiFile = input("Put your file in the same folder. What is the name of your file? (Include .txt)")

#checking file format
if ".txt" in uiFile:
    FILENAME=uiFile
else:
    print("Invalid Syntax: Try Again")

#Reading file
wordData = pd.read_csv(FILENAME)
wordCount = wordData.count(int())

#Row Column Check
for i in range(wordData):
    temp=[]
    for j in range(0,10):
        temp+=(f"{i}{j} ")
    print(temp)

#Word Search Function
  
for i in range(11):
    for j in range(11):
        i+=1
        j+=1
        if i >=11 or j>=11:
            break
        print(f"{i-1}{j-1}",end=" ") 
    print()
   
for i in range(10):
    for j in range(10):
        if i >=10 or j>=10:
            break
        print(f"{j}{i}",end=" ") 
        i+=1
        j+=1
    print() 
    
