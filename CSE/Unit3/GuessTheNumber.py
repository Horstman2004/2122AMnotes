import random
secretnumber=random.randint(0,100)
print(secretnumber)
ui=(input("Guess a number"))
strike=1
correctanswer=False

while (strike!=3 and not correctanswer):
    #while the ui has not given us a number
    ui=input("Guess a number?")
    while(not ui.isdigit()):
        #   keep asking for a number
        ui=input("Guess a number?")
    if secretnumber==int(ui):
        print('You got it')
        correctanswer=True
    elif secretnumber < int(ui):
        print("You're too high")
    elif secretnumber > int(ui):
        print("You're too low")
    else:
        print("Sorry but you FAILED")   
    strike+=1