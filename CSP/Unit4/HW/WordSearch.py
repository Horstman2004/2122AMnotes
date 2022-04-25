#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Varibles
"""#User Interface
uiFile = input("Put your file in the same folder. What is the name of your file? (Include .txt)")

#checking file format
if ".txt" in uiFile:
    FILENAME=uiFile
else:
    print("Invalid Syntax: Try Again")"""

FILENAME = "Book1.csv"
wordData = pd.read_csv(FILENAME)
wordCount = wordData.count(int())
print(wordData)

#Row Column Check
for i  in wordData:
    temp=[]
    for j in wordData:
        temp+=(f"{i}{j} ")
    print(temp)

#Word Search Function
for i in wordData:
    for j in wordData:
        i+=1
        j+=1
        if i >=100 or j>=100:
            break
        print(f"{i-1}{j-1}",end=" ") 
    print()
   
for i in wordData:
    for j in wordData:
        if i >=100 or j>=100:
            break
        print(f"{j}{i}",end=" ") 
        i+=1
        j+=1
    print() 
    
