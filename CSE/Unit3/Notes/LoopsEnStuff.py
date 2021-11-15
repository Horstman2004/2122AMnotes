#while something is true:
#   do something
#while (boolean expression is == true):
#   do
#   this
#   algorithm
#iterable vriable - a varible we add some value to

#i=0 #n or 1
#while (i<0):    #< > or <= >=
    #print(i)
    #i+=1

#i+10000
#while(i>+1000):
    #print(i)
    #i-=5


#ui = input("Guess What?")
#while(ui!="WHAT" and ui!="WAT" and ui!="WHEAT" and ui!="WATT" and ui!="WUT"):
#    ui = input("Guess What?")
#print("Chicken Butt")

'''
correctAnswers=["yes", "no", "y", "n", "yeaper", "sure", "YAAAAAS"]
ui = input("WOuld you like an apple pie with that?")
while(not(ui in correctAnswers)):
   ui = input("Would you like and apple pie with that?")
print("Ding fries are done!")

#Challenge 1
total=[]
ui=input("Enter in numbers")
while(ui!="stop"):
    total.append(float(ui))
    ui=input("Enter in numbers")
    print(sum(total))
'''

#Challenge 2
ui=input("give me a numba")
numberofevens=0
numberofodds=0
while(ui!=0):
    ui=int(input("give me a numba"))
    if(ui%2==0):
        numberofevens+=1
    elif(ui%2==1):
        numberofodds+=1
print(numberofevens)
print(numberofodds)
