import datetime #do anything with time, use this module
passwordtocheck = "aeN281"
begintime = datetime.datetime.now()
#generate new password
cpuguess = 0
havenotguessedthepassword = True
while(havenotguessedthepassword):
#check to see if it is equal
    if cpuguess == passwordtocheck:
        print(f"Got it: {cpuguess}")
        havenotguessedthepassword = False
    else:
        cpuguess+=1
#if not generate new
endtime = datetime.datetime.now()
print(endtime-begintime)