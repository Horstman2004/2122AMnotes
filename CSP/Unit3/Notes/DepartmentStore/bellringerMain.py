import matplotlib.pyplot as plt
import pandas

FILENAME = "MOCK_DATA.csv"
tempData = pandas.read_csv(FILENAME)
tempCount = tempData.count(int())
pandas.set_option('display.float_format', str)

us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

states = tempData.state.unique()
print(states)

for i in states:
    if i in us_states:
        us_states.remove(i)
        print(i,us_states)
print(us_states)

finalData = open("Missing_US_States.txt","w")
finalData.writelines(f"There is no missing states in the csv file.")
finalData.close()