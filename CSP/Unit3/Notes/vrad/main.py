import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "vins.csv"
df = pandas.read_csv(FILENAME,header=0)
cleanData=df["JTHBL5EFXF5390397"].tolist()

badLetters=["I","O","Q","W"]
cleanVins=[]

for i in cleanData:
    tempList=list(str(i))
    print(tempList)
    if badLetters in tempList:
        cleanVins.append(i)
print(cleanVins)