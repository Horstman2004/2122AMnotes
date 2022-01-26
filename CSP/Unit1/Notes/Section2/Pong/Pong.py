#imports
import turtle as t

#game config
COURT_HEIGHT = 600
COURT_WIDTH = 1000
PADDLE_WIDTH = 45

#turtle generation
wn = t.Screen()
wn.setup(width=.7,height=.8)
border = t.Turtle(visible=False)    #same as hideturtle

#leftplayer - redplayer
leftPlayer = t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.setx(-COURT_WIDTH/2)         #set the padle on the left side of the court
leftPlayer.turtlesize(4,1)              #turns a square into a rectangle

#rightplayer - blueplayer
rightPlayer = t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(COURT_WIDTH/2)         #set the padle on the left side of the court
rightPlayer.turtlesize(4,1)             #turns a square into a rectangle

#functions
def draw_field():
    wn.bgcolor("gray")
    border.speed(0)
    border.pensize(3)
    border.penup()
    border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.penup()
    border.sety(-COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_WIDTH)
    border.penup()
    border.setposition(0,-COURT_HEIGHT/2)
    border.pendown()
    border.setheading(90)
    border.pensize(1)
    for i in range(COURT_HEIGHT//50):   #// returns int value for range
        border.forward(26)
        border.penup()
        border.forward(26)
        border.pendown()

def upLeft():
    y=leftPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        leftPlayer.sety(y+10)

def downLeft():
    y=leftPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        leftPlayer.sety(y-10)

def upRight():
    y=rightPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        rightPlayer.sety(y+10)

def downRight():
    y=rightPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        rightPlayer.sety(y-10)

#main game loop and events  
wn.listen()
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"e")
wn.onkeypress(downRight,"d")
 
draw_field()

wn.mainloop()