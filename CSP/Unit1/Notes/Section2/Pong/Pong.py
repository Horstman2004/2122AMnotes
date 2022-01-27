#imports
import turtle as t
import random as random

#game config
COURT_HEIGHT = 600
COURT_WIDTH = 1000
PADDLE_WIDTH = 45
BALL_SIZE = 15
speed = 10
leftScore = 0
rightScore = 0
fontSettings = "Arial"

#turtle generation
wn = t.Screen()
wn.setup(width=.7,height=.8)
border = t.Turtle(visible=False)    #same as hideturtle

#ball config
ball = t.Turtle()
ball.penup()
ball.speed(speed)
ball.shape("circle")

#leftplayer - redplayer
leftPlayer = t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.setx(-COURT_WIDTH/2)         #set the padle on the left side of the court
leftPlayer.turtlesize(4,1)              #turns a square into a rectangle

lScore = t.Turtle(visible=False)
lScore.speed(0)
lScore.penup()
lScore.setposition(-COURT_WIDTH/4,COURT_HEIGHT/4)
lScore.write(leftScore,font=fontSettings)

#rightplayer - blueplayer
rightPlayer = t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(COURT_WIDTH/2)         #set the padle on the left side of the court
rightPlayer.turtlesize(4,1)             #turns a square into a rectangle

rScore = t.Turtle(visible=False)
rScore.speed(0)
rScore.penup()
rScore.setposition(COURT_WIDTH/4,COURT_HEIGHT/4)
rScore.write(rightScore,font=fontSettings)

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

def resetBall():        #debugging / gameover
    ball.setposition(0,0)
    if random.randint(0,1) == 0:
        ball.setheading(random.randint(135,225))        #set heading for direction
    else:
        ball.setheading(random.randint(-45,45))

def collidedWithPaddle(paddle,b):       #passing in the paddle and ball turtles
    #this f(x) will check if the given ball and paddle collide
    if paddle.distance(b) < PADDLE_WIDTH:
        b.setheading(180-b.heading()) 
        if b.xcor()>0:              #on the right side of the court
            b.setx(b.xcor()-5)     #cheat to keep ball out of the paddle
        else:
            b.setx(b.xcor()+5)      #cheat to keep the ball out of the paddle
        b.forward(speed)
        

def move():             #reseting the ball's x,y
    global leftScore,rightScore
    ball.forward(10)
    x,y = ball.position()
    #did it hit the top or bottom
    if y>(COURT_HEIGHT/2-BALL_SIZE) or y<(-COURT_HEIGHT/2-BALL_SIZE):
        ball.setheading(-ball.heading())
    #did it hit an edge
    elif x>(COURT_WIDTH/2) or x<(-COURT_WIDTH/2):
        if x>-COURT_WIDTH/2:
            leftScore+=1
            lScore.clear()
            lScore.write(leftScore,font=fontSettings)
        elif x<COURT_WIDTH/2:
            rightScore+=1
            rScore.clear()
            rScore.write(rightScore,font=fontSettings)
        resetBall()
    #did it hit a paddle
    else:
        collidedWithPaddle(leftPlayer,ball)
        collidedWithPaddle(rightPlayer,ball)
    wn.ontimer(move,20)



#main game loop and events  
wn.listen()
wn.onkeypress(resetBall,"r")
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"e")
wn.onkeypress(downRight,"d")
 
draw_field()
move()

wn.mainloop()