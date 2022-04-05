import pandas
pandas.set_option('display.max_rows', 50000)
pandas.set_option('display.max_columns', 50000)
pandas.set_option('display.width',5000)
#file was converted to csv through excel
FILENAME = "EVVWeatherOBS.csv"
tempData = pandas.read_csv(FILENAME)
tempCount = tempData.count(int())
print(tempData)

#Uniques list
TAVGuniq=[]
TOBSuniq=[]

#listing all values
TAVGall = list(tempData["Column6"])
TOBSall = list(tempData["Column9"])

#finding if there are values or not
for i in TAVGall:
    if "-9999" not in i:
        TAVGuniq.append(i)
#print(TAVGuniq)

for i in TOBSall:
    if "-9999" not in i:
        TOBSuniq.append(i)
#print(TOBSuniq)

#Final File
tempData = tempData.drop(columns="Column9")
finalData = open("EVVWeatherObs(Cleaned).txt","w")
finalData.writelines(f"""There is Data in the TAVG Column. However this is no data in the TOBS Column
                     {tempData}""")
finalData.close()

print(tempData)

