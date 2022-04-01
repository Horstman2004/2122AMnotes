#My way using pandas
import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "MOCK_DATA.csv"
tempData = pandas.read_csv(FILENAME)
tempCount = tempData.count(int())
pandas.set_option('display.float_format', str)
print(tempData)

#states = tempData['state'].value_counts()
departments = tempData.department.unique()
IPSList = list(tempData["ip"])
#cost = tempData['cost'].total()
#companies = tempData['company'].value_counts()
print(IPSList)

#Lists
departmentsList=[]
costList=[]
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

#Erasing Purchases with bad IPS

print(badIPS)
print(badIPIndex)

#Finding Min and Max Values
depTotal =[]
for i in departments:
    p = tempData.loc[tempData.department == i,"cost"]
    total = p.sum()
    total.round()
    departmentsList.append(i)
    costList.append(total)
    print(i,total)
    depTotal.append((i,total))

totals = []
for tup in depTotal:
    totals.append(tup[1])
totals.sort()
minVals = totals[:5]
maxVals = totals[-5:]
print(minVals)
print(maxVals)
minDeps = []
for val in minVals:
    for tup in depTotal:
        if val == tup[1]:
            minDeps.append(tup[0])
            
maxDeps = []
for val in maxVals:
    for tup in depTotal:
        if val == tup[1]:
            maxDeps.append(tup[0])
      
print(minDeps)
print(maxDeps)
    
    
#Fake Ip Finder 1st Iteration   
"""
invalidCharacter="."
for k in ip:
        if k != invalidCharacter:
            numbers.append(k)
        elif k == invalidCharacter:
            p = "".join(map(str, numbers))
            if p not in fakeIPS:
                #print(f"Valid IP: {p}")
                numbers.clear()
            elif p in fakeIPS:
                #print(f"Fake IP: {p}")
                badIPS.append(numbers)
                numbers.clear()"""




#Litte UI
def userInterface():
    ui = input(str(f'''
                -----------------------------------------
                Choose what statistics you want to see...
                -----------------------------------------
                Top 5 Departments: T5
                Bottom 5 Departments: B5
                Student Purchases: SP
                Visa or Mastercard: VM
                -----------------------------------------
                '''))
    if ui == "T5" or "t5":
        max()
    elif ui == "B5" or "b5":
        min()
    elif ui == "SP" or "sp":
        studentPurchases()
    elif ui == "VM" or "vm":
        visaMastercard()
    else:
        print(f"""
            -------------------------
            Invalid Input: {ui}
            -------------------------
            Valid Inputs Below...
            -------------------------
            Top 5 Departments: T5
            Bottom 5 Departments: B5
            Student Purchases: SP
            Visa or Mastercard: VM
            -------------------------
            """)


#UI Functions
def min():
    #Min Value Graphs
    plt.bar(minDeps,minVals)
    plt.ylabel("Sales Per Million")
    plt.xlabel("Department")
    plt.title("Bottom 5 Sales")
    plt.show()
    
def max():
    #Max Value Graphs
    plt.bar(maxDeps,maxVals)
    plt.ylabel("Sales Per Million")
    plt.xlabel("Department")
    plt.title("Top 5 sales")
    plt.show()

def studentPurchases():
    return

def visaMastercard():
    return



#Other Iterations
"""for i in costList:
    maxVal = max(costList)
    top5cost.append(maxVal)
    index = costList.index(maxVal)
    costList.remove(maxVal)
    top5deps.append(departments[index])

print(top5cost)
print(top5deps)"""

"""print(f'''
States: 
{states}
Department: 
{departments}
Company: 
{companies}
      ''')"""

"""
#Different Way
with open("MOCK_DATA.csv") as f:
    file=f.readlines()
    
uniqueStates=[]
for line in file:
    time,ip,email,state,junk = line.split(",")
    if not (state in uniqueStates):
        uniqueStates.append(state)
#print(len(uniqueStates))
#print(uniqueStates)
#ANSWER: All states were present based on the print out of two lines above

#Another Way
import pandas as pd
data = pd.read_csv("MOCK_DATA.csv",header=0)
#find unique values
states = []
for i in data["state"]:
    if not (i in states):
        states.append(i)
"""