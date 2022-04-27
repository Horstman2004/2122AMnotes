#My way using pandas
import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "MOCK_DATA.csv"
tempData = pandas.read_csv(FILENAME)
tempCount = tempData.count(int())
pandas.set_option('display.float_format', str)
IPSList = list(tempData["ip"])
print(tempData)

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

#Erasing Purchases with bad IPS
for i in badIPIndex:
    tempData.drop(i-1,axis=0,inplace=True)
print(tempData)

#states = tempData['state'].value_counts()
departments = list(tempData.department.unique())
#cost = tempData['cost'].total()
#companies = tempData['company'].value_counts()
print(departments)

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

#Student Purchases
dataCount=0
allDeps=[]
departmentTotal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
departmentSumTotal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for k in tempData['email']:
    dataCount+=1  
    if '.edu' in k:
        allDeps.append(k)
        for j in range(1):
            studentDepPurchase = tempData.loc[tempData.email == str(k)]
            studentDep = tempData['department'].values[dataCount]           #Grabbing the Department that the student bought from
            studentCost = tempData['cost'].values[dataCount]                #Grabbing just the cost none of the "float 64 Name: Cost:"
            index = departments.index(studentDep)
            num = departmentTotal.pop(index)
            num+=1
            index-=1
            departmentTotal.insert(index,num)
            departmentStrTotal=[str(int) for int in departmentTotal]        #Turns list of ints to list of strings
            print(departmentTotal)
            
for i in allDeps:
    index1 = departments.index(studentCost)
    num1 = departmentSumTotal.pop(index)       
    num1+=studentCost
    index1-=1      
    departmentSumTotal.insert(index1,num1)      
    departmentStrSumTotal=[str(int) for int in departmentSumTotal]  #Turns list of ints to list of strings
           
#Visa or Mastercard



    

#Functions
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

def studentPurchasesGraph():
    plt.bar(departmentStrTotal,departments)
    plt.ylabel("Number of Student Purchases Per Department")
    plt.xlabel("Departments")
    plt.title("Student Purchases Per Department")
    plt.show()
    
    plt.bar(departmentStrSumTotal,departments)
    plt.ylabel("Departments")
    plt.xlabel("Student Purchases Sum")
    plt.title("Sum of Student Purchases Per Department")
    plt.show()
studentPurchasesGraph()

    
def visaMastercard():
    return


