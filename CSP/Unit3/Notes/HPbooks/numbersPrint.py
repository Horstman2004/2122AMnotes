#relative file path -> the path from your file to another file
with open("numbers.txt","r",encoding="utf8") as f:
    file = f.readlines()
    
reducedFile=[]
for line in file:
    if line != "\n":
        reducedFile.append(line)
print(reducedFile)

with open("numbers.text","w+",encoding="utf8") as f:
    for line in reducedFile:
        f.write(line)
print("reduced length of file: ",len(reducedFile))  