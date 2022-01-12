#-----Imports-----
import random as r

#-----Varibles & Lists-----
endgame = False
guessingwords=["ELEPHANT","TURTLE","PYTHON"]    #list of guessing words
word = r.choice(guessingwords)  #chooses random word from list
strikes = 0 # # of strikes
correctletters=[]
blanks=''
list(word)

#-----Loops and Functions-----
while endgame != True or strikes == 6:
    for i in range(len(word.upper())):  #   Grabs length of word to put the correct # of _
        correctletters.append("_ ")
        blanks+="_ "
    print(blanks,end='')  #grabs last item in list / removes all the brackets commas and quotes
    
    #turns "word" into a list
    listy=[]
    for i in range(len(word)):
        listy.append(word[i])
    
    #Guess a number, auto uppercase, is alphabetical character, or is in listy/word.
    
    while endgame != True or strikes == 6:
        print("\n""Guess a letter.")
        ui=input()
        ui = ui.upper()
        if correctletters == listy: #cross checks listy and correctletters to see if they are =
            endgame=True
            print("You Won")
            break
        elif ui.isalpha():    #check if is alphabetical character
            if ui in listy:
                for i in range(len(listy)):
                    if listy[i] == ui:  #if one of listys indexs is = to ui it appends that letter
                        correctletters[i]=(ui)
            elif ui not in listy:   #either adds a strike or ends the game and breaks the loop depending on strikes
                if strikes != 5:
                    print("Wrong")
                    strikes+=1
                    print("You have", strikes, " strikes")
                else:
                    print("You failed to guess my word!")
                    endgame = True
                    break
        print (" ".join(correctletters)+"\n")
    break
        
        
    
            
            
            
            
            
            
            