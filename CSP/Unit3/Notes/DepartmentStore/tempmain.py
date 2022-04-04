#My way using pandas
import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "MOCK_DATA.csv"
dirtyData = pandas.read_csv(FILENAME)
tempCount = dirtyData.count(int())
pandas.set_option('display.float_format', str)
IPSList = list(dirtyData["ip"])

#Lists
fakeIPS=['0','192','127','255']
badIPS=[]
loopTime=0
badIPIndex=[]

#Finding Fake IPs
for i in (IPSList):
    numbers=[]      #Triple Digit
    numbers2=[]     #Single Digit
    #Finding IP index 
    for k in range(1):      #Looping once to grab values based on indexs
        numbers.append(i[:3])
        numbers2.append(i[0])
        loopTime+=1
        for i in numbers:   #Looping to see if there is a fake number
            if i in fakeIPS:
                print(f"Fake IP: {i}")
                badIPS.append(i)
                badIPIndex.append(loopTime)
        for i in numbers2:  #Looping to see if there is a fake number
            if i in fakeIPS:
                print(f"Fake IP: {i}")
                badIPS.append(i)
                badIPIndex.append(loopTime)
print(badIPIndex)

for i in badIPIndex:
    dirtyData.drop(i-1,axis=0,inplace=True)

print(dirtyData)




"""#turning strings to numbers
loopTimeStrings = [str(x) for x in badIPIndex]


#Erasing Purchases with bad IPS
lines = []
print(loopTimeStrings)
with open('MOCK_DATA.csv', 'r') as read_file:
    reader = pandas.read_csv(read_file)
    for row_number, row in enumerate(reader, start=1):
        if(row_number not in loopTimeStrings):
            lines.append(row)
            print(row)
with open('MOCK_DATA', 'w') as write_file:
    writer = pandas.read_csv(write_file)
    print(writer)"""