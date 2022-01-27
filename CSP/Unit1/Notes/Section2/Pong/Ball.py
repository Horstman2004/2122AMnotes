import random as random
import turtle as t


COURT_HEIGHT = 600
COURT_WIDTH = 1000
BALL_SIZE = 15
speed = 10

wn = t.Screen()
wn.setup(width=.7,height=.8)
border = t.Turtle(visible=False)    #same as hideturtle

ball = t.Turtle()
ball.penup()
ball.speed(0)
ball.shape("circle")

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
    border.penup()
    border.goto(-COURT_WIDTH/2,COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_HEIGHT)
    border.penup()
    border.goto(COURT_WIDTH/2,-COURT_HEIGHT/2)
    border.pendown()
    border.backward(-COURT_HEIGHT)

def resetBall():        #debugging / gameover
    ball.setposition(0,0)
    if random.randint(0,1) == 0:
        ball.setheading(random.randint(135,225))        #set heading for direction
    else:
        ball.setheading(random.randint(-45,45))
        
def move():     #reseting the ball's x,y\
    ball.forward(20)
    x,y = ball.position()
    #did it hit the top or bottom
    if y>(COURT_HEIGHT/2-BALL_SIZE) or y<(-COURT_HEIGHT/2-BALL_SIZE):
        ball.setheading(-ball.heading())
    #did it hit an edge
    elif x>(COURT_WIDTH/2) or x<(-COURT_WIDTH/2):
        resetBall()
    #did it hit a pattern
    wn.ontimer(move,20)

draw_field()
move()

wn.listen
wn.onkeypress(resetBall,"r")
wn.mainloop()