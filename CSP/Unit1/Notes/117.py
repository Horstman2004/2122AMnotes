'''
    Sequences:
        string - "concatenated data"
        List - "list of data that can be different types"
        Tuple - immutable or they can change
        Array - immutable or they can change
        *Dictoinaries
'''

import turtle as t
import random as r


shapes=["arrow", "turtle", "circle", "square", "triangle", "classic"]
colors=["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
myturds=[]



for s in range(len(shapes)):
    #                       Keyword parameter shape is a characteristic of your turtle
    bob = t.Turtle(shape=shapes[s])
    bob.fillcolor(colors[s])    #color of the turtle
    myturds.append(bob)
#loop throught your turtles and space thm out from the middle to the top right
x=0
y=0
t.goto(x,y)
for i in (myturds):
    i.pencolor(colors.pop())    #grabs first item from list
    x+=25
    y+=25
    i.penup()
    i.goto(x,y)
    i.pendown()
    i.color(r.choice(colors))   #makes random color choice
    

print(myturds)

wn=t.Screen()
wn.mainloop()
