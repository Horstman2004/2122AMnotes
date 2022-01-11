import turtle as t

hori=[]
vert=[]

shapes=['arrow','turtle','circle','square','triangle','classic']
hcolors=['red','blue','green','orange','purple','gold']
vcolors=['magenta','black','darkred','yellow','lime']

loc=-100

for s in shapes:
#hori
    leonardo=t.Turtle(shape=s)
    leonardo.speed(0)
    hori.append(leonardo)
    leonardo.penup()
    c='red'
    leonardo.fillcolor(c)
    leonardo.goto(-200,loc)
    leonardo.setheading(0)
#vert
    bert=t.Turtle(shape=s)
    bert.speed(0)
    vert.append(bert)
    bert.penup()
    c='blue'
    bert.fillcolor(c)
    bert.goto(-loc,200)
    bert.setheading(270)
    loc+=50
    
    
#moving turtles

iterations=0

while len(vert)>0:
    #move the turtle
    for h in hori:
        h.forward(5)
    for v in vert:
        v.forward(5)
    #check for collision
    #if h and v overlap, then collision
    if (abs(h.xcor() - v.xcor()) <10):
        if abs((h.ycor() - v.ycor()) <10):
            print(h.xcor(),h.ycor(),v.xcor(),v.ycor())
            h.fillcolor('white')
            v.fillcolor('white')
            hori.remove(h)
            vert.remove(v)
    iterations+=1
wn=t.Screen()
wn.mainloop()