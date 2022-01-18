#-----import statements-----
import turtle as t
import random as r
import leaderboard as lb

#-----Leaderboard-----------
FILENAME = "leaderboard.txt"
#read, write or append
#write - overwrites all data
#append - will add data to the bottom of the file
with open(FILENAME, "r") as f:
    file = f.readlines()    #file is a list of the data
    f.close()

#-----game configuration----
wn = t.Screen()
SCREENW,SCREENH = 300,300
score=0
timer=5
timesUp=False
counterInterval = 1000
#tuple variable = ("fontstyle",fontsize,"font (B,I,U)")
fontSetup=("Comic Sans MS", 30, "normal")

#-----initialize turtle-----
mo = t.Turtle()
mo.shape("turtle")
mo.shapesize(2)
mo.fillcolor("brown")
mo.speed(0)

scorekeeper = t.Turtle()
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.speed(0)

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100,165)
counter.pendown()
counter.speed(0)
#-----game functions--------
def updateHS():
    with open(FILENAME,"a") as f:
        f.write("AAA,10")
        f.close()
    
def countdown():
    global timer, timesUp
    counter.clear()
    if timer<=0:
        counter.write("Times Up!",font=fontSetup)
        timesUp=True
        #updateHS()
        manageLeaderboard()
    else:
        counter.write(f'Time: {timer}',font=fontSetup)
        timer-=1
        counter.getscreen().ontimer(countdown,counterInterval)
        print(timer)

def updateScore():
    global score
    #it will see the var score in other parts of the program
    score+=1
    scorekeeper.clear()      #clear what it already wrote
    #write the score
    scorekeeper.write(f"Score: {score}",font=fontSetup)
     
def changePosition():
    #move the turtle to a random location on the screen
    newX = r.randint(-SCREENW/2,SCREENW/2)
    newY = r.randint(-SCREENH/2,SCREENH/2)
    mo.color("white")
    mo.pencolor("red")
    mo.stamp()
    mo.pencolor("black")
    mo.color("blue")
    mo.penup()         #doesn't leave a trail
    mo.hideturtle()    #don't see where it is going
    mo.goto(newX,newY)
    mo.showturtle()
    mo.pendown()


#read in the top 5 high scores and draw it on the screen
def manageLeaderboard():
    global score
    global scorekeeper
    
    #parallel list --> smae length and corrosponding data based on the index
    namesList = lb.get_names(FILENAME)
    scoresList = lb.get_scores(FILENAME)
    
    #show the lb w/ or w/o the current player
    print("namesList",namesList)
    print("scoresList",scoresList)
    




#no matter what, if it is a mouse click
#    pass in x and y
def moClicked(x,y): 
    #x and y are the cuursor's coordinates
    print(x,y)
    print("mo was clicked")
    changePosition()
    updateScore()


#-----events----------------
#obj.method(command or function name)

wn.ontimer(countdown,counterInterval)     #"acts" like the clock widget from MIT
mo.onclick(moClicked)
wn.mainloop()