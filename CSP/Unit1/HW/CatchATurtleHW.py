#-----import statements-----
from operator import truediv
import turtle as t
import random as r

#-----game configuration----
wn = t.Screen()
SCREENW,SCREENH = 300,300
score=0
timer=5
timesUp=False
countdownstart=True
counterInterval = 1000
click=0
#tuple variable = ("fontstyle",fontsize,"font (B,I,U)")
fontSetup=("Comic Sans MS", 30, "normal")

#-----initialize turtle-----
mo = t.Turtle()
mo.shape("turtle")
mo.fillcolor("brown")
mo.speed(0)
mo.hideturtle()


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

accuracytxt = t.Turtle()
accuracytxt.hideturtle()
accuracytxt.penup()
accuracytxt.goto(100,130)
accuracytxt.pendown()
accuracytxt.speed(0)
#-----game functions--------
def countdown2():
    global timer, timesUp
    counter.clear()
    if timer<=0:
        counter.write("Start",font=fontSetup)
        timer+=5
        countdown1()
        mo.showturtle()    
    else:
        counter.write(f'Time: {timer}',font=fontSetup)
        timer-=1
        counter.getscreen().ontimer(countdown2,counterInterval)
        print(timer)

def countdown1():
    global timer, timesUp
    counter.clear()
    if timer<=0:
        counter.write("Times Up",font=fontSetup)
        timesUp=True
        mo.hideturtle()
    else:
        counter.write(f'Time: {timer}',font=fontSetup)
        timer-=1
        counter.getscreen().ontimer(countdown1,counterInterval)
        print(timer)
                
def updateScore():
    global score
    #it will see the var score in other parts of the program
    score+=1
    scorekeeper.clear()      #clear what it already wrote
    #write the score
    scorekeeper.write(f"Score: {score}",font=fontSetup) 
    decreaseSize()

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
    wn.bgcolor("red")

#no matter what, if it is a mouse click
#    pass in x and y
def moClicked(x,y): 
#x and y are the cuursor's coordinates
    changePosition()
    updateScore()
    
def decreaseSize():
    size=mo.turtlesize()
    decrease = tuple([2 / num for num in size])
    mo.turtlesize(*decrease)
    wn.bgcolor("white") 
    
def clickAccuracy(x,y):
    global score, click
    click+=1
    accuracy= round((score/click)*100,0)
    mo.showturtle
    accuracytxt.clear()
    mo.clear()
    accuracytxt.write(f"Accuracy: {accuracy}%", font=fontSetup)
    
#-----events----------------
#obj.method(command or function name)
wn.onclick(clickAccuracy)
wn.ontimer(countdown2,counterInterval)      #"acts" like the clock widget from MIT
mo.onclick(moClicked)
wn.mainloop()