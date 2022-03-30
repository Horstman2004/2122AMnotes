#My way using pandas
import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "MOCK_DATA.csv"
tempData = pandas.read_csv(FILENAME)
tempCount = tempData.count(int())
pandas.set_option('display.float_format', str)

#states = tempData['state'].value_counts()
departments = tempData.department.unique()

#cost = tempData['cost'].total()
##companies = tempData['company'].value_counts()

#Lists
departmentsList=[]
costList=[]

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

#Min and Max Value Graphs
plt.bar(minDeps,minVals)
plt.ylabel("Sales Per Million")
plt.xlabel("Department")
plt.title("Bottom 5 Sales")
plt.show()
plt.bar(maxDeps,maxVals)
plt.ylabel("Sales Per Million")
plt.xlabel("Department")
plt.title("Top 5 sales")
plt.show()

#Fake IPs
fakeIPList=["0","192","127","255"]
IPList=[]



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