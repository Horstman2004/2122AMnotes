filename="TestData.csv"
classes=["Advanced","Engineer","Collision","Automotive Service","Construction","CISCO","Software","Culinary","Diesel","Electrical","Graphic","Health","HVAC","Precision","Public","Radio","Vet","Welding"]
#Advanced,Engineer,Collision,AutomotiveService,Construction,CISCO,Software,Culinary,Diesel,Electrical,Graphic,Health,HVAC,Precision,Public,Radio,Vet,Welding=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
listOfList=[]

for i in classes:
    listOfList.append([])

#with open(fileYouAreOpening,mode) as varibleName
with open(filename,"r") as file:
    #reads lines, returns a list
    listOfLines = file.readlines()

#shreads data to its appropriate list
for row in listOfLines:
    for i in range(len(classes)):
        if classes[i] in row:
            listOfList[i].append(row)
        
#write to the text file
for i in range(len(classes)):
    with open(f"{classes[i]}.csv","w") as fileToWrite:
        for row in listOfList[i]:
            fileToWrite.write(row)
    
    

