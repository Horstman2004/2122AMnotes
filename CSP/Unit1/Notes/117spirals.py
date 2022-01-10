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
    bob.penup
#loop throught your turtles and space thm out from the middle to the top right
x,y=0,0
t.goto(x,y)
direction=90
distance=50
for i in myturds:
    i.penup()
    i.goto(x,y)
    i.pendown()
    i.pencolor(colors.pop())    #grabs first item from list
    i.setheading(direction)
    i.right(45)
    i.forward(distance)
    x,y =i.xcor(),i.ycor()
    #i.color(r.choice(colors))   #makes random color choice
    direction = i.heading()
    distance+=10

print(myturds)

wn=t.Screen()
wn.mainloop()
