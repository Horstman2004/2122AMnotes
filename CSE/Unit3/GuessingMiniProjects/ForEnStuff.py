#mode = the one that recurrs the most
#min = smallest
#max = highest
#range = lowest to the highest
'''
range(10)
#generate a list of numbers from 0 up to the number in the ()
print(range(10))
#range(stat, stop, step)
print(range(0,10,2))
print(range(0,100))

#for i many times in range(number of times, I need it to run):
for i in range(0,10,2):
    print(i)

#print out odd numbers from 37 to 83
for i in range(37,84,2):
    print(i)

    #for someVarible in aList
    #   do something

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

name=["bob","ryan","will","wyatt","sydni","aidan","paige"]
for i in name:
    #every intertion -> i becomes that item in the list
    print(i)
'''

#number=[7,60,5,24,9,20,12,22,21,10]
#for i in range(len(number)):    #creates an index
    #print(i*2)                  #gets the item in the list @ the index
#print(number)







#algorithm that takes in user input
#   ask the user for 10 numbas
#   print out the total of those numbas
'''
total=0
for i in range(10):
    ui=input("give me a numba")
    total+=ui
print(total)

for i in range(999999**999999):
    ui = input("Guess What?")
    while(ui!="WHAT" and ui!="WAT" and ui!="WHEAT" and ui!="WATT" and ui!="WUT"):
        print("Chicken Butt")
        break
'''

name="jimbob"   #stings are sqeuences......... just like lists..........
for i in name:
    print(i)    #i is each letter
for i in range(len(name)):
    print(name[i])  #i is the index for each letter 

name="SpongeBob SquarePants"
numberofvowels=0
#loop through the name
for i in name:
#   check to see if the letter is a vowel
    if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        numberofvowels+=1
#       if so, count it
print(numberofvowels)

numberofvowels=0
vowels=["a","e","i","o","u"]
for i in name:
    if i in vowels:
        numberofvowels+=1
print(numberofvowels)