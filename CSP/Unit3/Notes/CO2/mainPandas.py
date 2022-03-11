import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "temperature_data.csv"
tempData = pandas.read_csv(FILENAME,header=0)
tempCount = tempData.count(int())
#header=0 stes the dirst row as the "headers"

#min
min = tempData["Anomaly"].min()
#max
max = tempData["Anomaly"].min()
#mean
mean = tempData["Anomaly"].mean()
#sum
sum = tempData["Anomaly"].sum()
#average
average = tempData["Anomaly"].sum()/(tempCount)

#plot
plt.plot(tempData["Year"],tempData["Anomaly"])
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in Temperature")
plt.show()

#print out
print(f'''
      Min: {min}
      Mean: {mean}
      Max: {max}
      Sum: {sum}
      Average: {average}
      ''')