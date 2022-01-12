import datetime as dt
#ask the user for what year they were born in
uy = int(input("What year were you born in?"))
um = int(input("What month were you born in?"))
ud = int(input("What day were you born?"))
#uii = input("What month were you born in?")
#print out how long ago that was

year = dt.datetime.now().year
month = dt.datetime.now().month
day = dt.datetime.now().day


if um > month:
    ageinMonths = (((year - 1) - uy))
