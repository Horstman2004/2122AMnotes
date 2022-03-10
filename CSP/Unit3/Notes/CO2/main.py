anomaliesList=[]


with open("temperature_data.csv","r") as f:
    file=f.readlines()

for i in range(len(file)):
    file[i]=file[i].rstrip(",")
    anomalies = [int(item) for item in file]
    anomaliesList.append(anomalies)
print(file)
    
"""for r in file:
    row=r.strip(",")
    a=row[1]
    anomaliesList.append(int(a))"""

minValue=min(anomaliesList)
maxValue=max(anomaliesList)
averageValue=sum(anomaliesList)


print(f'''
      min anomaly: {minValue}
      max anomaly: {maxValue}
      average anomaly: {averageValue}
      
      ''')