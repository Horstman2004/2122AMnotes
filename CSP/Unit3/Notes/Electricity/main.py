import matplotlib.pyplot as plt
import pandas

#read in the csv 
FILENAME = "elec_access_data.csv"
df = pandas.read_csv(FILENAME,header=0)

#find the unique countries and how many 
uniqueCountries = df.Entity.unique()
ourCountries=["United States","Bahamas","Mexico","Cuba","Canada"]

#graph the pur countries
#go find each of our countries in the unique countries
for c in uniqueCountries:
    if c in ourCountries:
        #grab the data of that particular country
        #x axis data
        years = df[df["Entity"]==c]['Year']
        #if the column is equal our country, make a dataframe of the years
        #y axis data
        elecAccess = df[df["Entity"]==c]['Access']
        #if the entity column is equal our country, make a dataframe of the access
        
        #since we are putting multiple countries in one graph 
        #plot our graph
        plt.plot(years,elecAccess,label=c)

plt.ylabel("% of Country Population")
plt.xlabel("Years")
plt.title("% of the Population with Electricity Access")
plt.legend()
plt.show()



"""entitiesList=[]
accessList=[]

entities = tempData.Entity.unique()
access = tempData["Access"]

for i in entities:
    entitiesList.append(i)
    
for i in access:
    access.append(i)

plt.plot(entitiesList,tempData["Access"])
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in Temperature")
plt.show()"""