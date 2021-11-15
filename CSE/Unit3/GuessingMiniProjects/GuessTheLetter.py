import random
secretnumber=chr(random.randint(65,90))
print(secretnumber)
ui=(input("Guess a number"))
strike=0
correctanswer=False

while (strike!=3 and not correctanswer):
    ui=input("Guess a number?")
    #while the ui has not given us a number
    while(not ui.isalpha()):
        #   keep asking for a number
        ui=input("Guess a number?")
    if ord(secretnumber)==ord(ui):
        print('You got it')
        correctanswer=True
    elif ord(secretnumber) < ord(ui):
        print("You're too high")
    elif ord(secretnumber) > ord(ui):
        print("You're too low")
    else:
        print("Sorry but you FAILED")   
    strike+=1