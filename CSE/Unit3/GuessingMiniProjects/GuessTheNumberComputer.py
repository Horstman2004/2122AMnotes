import random
secretnumber=int(input("Guess a number btwn 0-10000")) #User sets Number
correctanswer=False
while (not correctanswer):
    computerguess=random.randint(0,10000) #computer guesses a number
    if secretnumber==computerguess:
        print('CPU got it')
        print(computerguess)
        correctanswer=True
    elif secretnumber < computerguess:
        print("CPU too high")
        print(computerguess)
    elif secretnumber > computerguess:
        print("CPU too low")
        print(computerguess)
    else:
        print("Sorry but CPU FAILED")   