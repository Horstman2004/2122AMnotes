import turtle as t 

#varibles


#Screens
mainScreen = t.Screen()
mainScreen.screensize(canvheight=400,canvwidth=200)

#Turtles
PvC = t.Turtle()
PvP = t.Turtle()
Directions = t.Turtle()
Credits = t.Turtle()

#lists
wordingList=["PvC","PvP","Directions","Credits"]
turtles=[PvC,PvP,Directions,Credits]

#Turtle Config
for i in turtles:
    i.shapesize(2)
    i.shape("square")
    i.speed(0)
    i.color("blue")
    i.penup()

#Positions
PvC.goto(0,125)
PvP.goto(0,40)
Directions.goto(0,-40)
Credits.goto(0,-125)

#functions
"""def splitTurts():
    global Credits,Directions,PvP,PvC
    for i in range(len(turtles)):
        currentTurt = turtles.index[i]
        if i == 0:
            Credits = currentTurt
        elif i == 1:
            Directions - currentTurt
        elif i == 2:
            PvP = currentTurt
        elif i == 3:
            PvC = currentTurt
splitTurts()
print(Credits,Directions,PvC,PvP)"""

def onClick():
    PvC.onclick(gameMode(1))
    PvP.onclick(gameMode(2))
    Directions.onclick(gameMode(3))
    Credits.onclick(gameMode(4))  
    return

def gameMode(num):
    if num == 1:
        pvc()
    elif num == 2:
        pvp()
    elif num == 3:
        directions()
    elif num == 4:
        credits()
    else:
        print(f'onClick function Error and/or turtle Error...')
        mainScreen.bye()
    return

def pvc():
    
    mainScreen.update()
    return

def pvp():
    
    mainScreen.update()
    return

def directions():
    
    mainScreen.update()
    return

def credits():
    
    mainScreen.update()
    return

#loop
mainScreen.listen(
    PvC.onclick(gameMode(1))
    PvP.onclick(gameMode(2))
    Directions.onclick(gameMode(3))
    Credits.onclick(gameMode(4))  
)
mainScreen.mainloop()
