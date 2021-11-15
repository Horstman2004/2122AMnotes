import random
secretnumber=int(input("Guess a number btwn 0-100")) #User sets Number
correctanswer=False
computeranswers=[]
while (not correctanswer):
    computerguess=random.randint(0,2) #computer guesses a number
    ui=input(f"The CPU guessed: {computerguess} - (h,c,l) (ls to list previous answers)")
    computeranswers.append(str(computerguess))

    if ui=="c":
        print('CPU got it',computerguess)
        correctanswer=True
    elif ui=="h":
        print('CPU too high',computerguess)
        highest=computerguess-1
    elif ui=="i":
        print("CPU too low",computerguess)
        lowest=computerguess+1
    elif ui=="ls":
        print(computeranswers)