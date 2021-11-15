filename="TestData.csv"
classes=["Advanced","Engineer","Collision","Automotive Service","Construction","CISCO","Software","Culinary","Diesel","Electrical","Graphic","Health","HVAC","Precision","Public","Radio","Vet","Welding"]
Advanced,Engineer,Collision,AutomotiveService,Construction,CISCO,Software,Culinary,Diesel,Electrical,Graphic,Health,HVAC,Precision,Public,Radio,Vet,Welding=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

#with open(fileYouAreOpening,mode) as varibleName
with open(filename,"r") as file:
    #reads lines, returns a list
    listOfLines = file.readlines()

for row in listOfLines:
    #rstrip() removes the \n on the end of the row
    #split() splits the row based on a character
    if classes[0] in row:
        Advanced.append(row)
        
    #rowsplitter = row.split("\t",7)
    #print(rowsplitter)
#print(listOfLines)

with open("Advanced.csv","w") as fileToWrite:
    for row in Advanced:
        fileToWrite.write(row)