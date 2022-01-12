#-----Import Statements-----
import turtle as t
import random as r

#-----Game Configuration----
wn = t.Screen()


#-----Initialize Turtle-----
mo = t.Turtle()
mo.shape("turtle")
mo.shapesize(2)
mo.fillcolor("brown")


#-----Game Functions--------

def changePosition():
    #move the turtle to a random location on the screen
    screenw,screenh = 300,300
    newX = (r.randint(-screenw/2,screenw/2))
    newY = (r.randint(-screenh/2,screenh/2))
    mo.penup()
    mo.hideturtle()
    mo.goto(newX,newY)
    mo.showturtle()
    mo.pendown()
    
    


def moClicked(x,y):
    print(x,y)
    print("mo was clicked")
    changePosition()
    
    
#-----Events----------------
#obj.method(command or function name)
mo.onclick(moClicked)
wn.mainloop()

