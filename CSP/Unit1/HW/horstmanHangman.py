import random as r


guessingwords=["ELEPHANT","TURTLE","PYTHON"]    #list of guessing words
word = r.choice(guessingwords)  #chooses random word from list
strikes = 0 # # of strikes
correctletters=[]
blanks=''
list(word)
print(word)

while strikes < 6:
    for i in range(len(word.upper())):  #   Grabs length of word to put the correct # of _
        correctletters.append("_ ")
        blanks+="_ "
    print(blanks,end='')  #grabs last item in list / removes all the brackets commas and quotes
    
    #turns "word" into a list
    listy=[]
    for i in range(len(word)):
        listy.append(word[i])
    print(listy)
    
    #Guess a number / auto uppercase
    endgame = False
    while endgame != True or strikes < 6:
        print("\t""Guess a letter.")
        ui=input()
        ui = ui.upper()
        if ui.isalpha():
            if ui in listy:
                for i in range(len(listy)):
                    if listy[i] == ui:
                        correctletters[i]=(ui)
            elif ui not in listy:
                print("Wrong")
                print(correctletters,end='')
            elif correctletters == listy:
                print(correctletters,end='')
                print("You Won")
        print(correctletters,end='')
    
        
        
    break
            
            
            
            
            
            
            