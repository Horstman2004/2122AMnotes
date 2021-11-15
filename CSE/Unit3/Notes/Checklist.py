readyList=[]
questionList=["Did you wake up?", "Did you get dressed with new clothes and not your pjs?", "Did you pet Fido?"]

while(len(questionList)):
    readyList.append(False)



#Keep asking same 3 questioons, until readyList is full of True:
while(False in readyList):
    total=0
    i=0
    while(i<len(questionList)):
        if (readyList[i]==False):
        #Check to see if the user entered y for the question
            ui=input(questionList[i])
        elif ui=="y":
        #Change the index of that question in the readylist to True
            readyList[i]=True
