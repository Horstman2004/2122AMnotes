import random as r


guessingwords=["elephant","turtle","python"]    #list of guessing words
word = r.choice(guessingwords)  #chooses random word from list
strikes = 0 # # of strikes

while strikes != 3:
    for i in range(str(word)):
        print("_")

