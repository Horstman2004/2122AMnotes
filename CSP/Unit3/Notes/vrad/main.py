import pandas

#read the file
FILENAME = "vins.csv"
df = pandas.read_csv(FILENAME,header=0)
cleanData=df["JTHBL5EFXF5390397"].tolist()

#lists
badLetters=["I","O","Q","W"]
cleanVins=[]

#Looping through to see if a letter is in the VIN. If not, appedn it to a cleanVINS list.
for j in cleanData:
    for i in badLetters:
        if i in j:
            print(f"Invalid VIN: {j}")
        else:
            cleanVins.append(j)
            print(f"Valid VIN: {j}")
