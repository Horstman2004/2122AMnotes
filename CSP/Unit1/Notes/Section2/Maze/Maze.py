from turtle import *
import random
import turtle

distance = 500
PATH_WIDTH = 20
NUMWALLS = 25

wn=Screen()
mazeDrawer = Turtle()
mazeDrawer.penup()
mazeDrawer.goto(100,-100)
mazeDrawer.pendown()
mazeDrawer.speed(0)
mazeDrawer.pensize(5)
mazeDrawer.setheading(90)



#game functions
def lookUp():
     mazeDrawer.setheading(90)
def lookDown():
     mazeDrawer.setheading(270)
def lookRight():
     mazeDrawer.setheading(0)
def lookLeft():
     mazeDrawer.setheading(180)
     
def drawDoor():
     mazeDrawer.forward(10)
     mazeDrawer.penup()
     mazeDrawer.forward(PATH_WIDTH*2)
     mazeDrawer.pendown()

def drawBarrier():
     mazeDrawer.forward(PATH_WIDTH*3)
     mazeDrawer.left(90)
     mazeDrawer.forward(PATH_WIDTH*2)
     mazeDrawer.backward(PATH_WIDTH*2)
     mazeDrawer.right(90)

#events and mainloop running code
lenghtOfTheWall = PATH_WIDTH
#draw the remain walls
for i in range(NUMWALLS):
     lenghtOfTheWall+=PATH_WIDTH
     #skip the first 4 walls
     if(i>3):
          
          #find when to draw a door
          door = random.randint(2*PATH_WIDTH, (lenghtOfTheWall-2*PATH_WIDTH))
          #find when to draw a barrier
          barrier = random.randint(2*PATH_WIDTH, (lenghtOfTheWall-2*PATH_WIDTH))
          
          #CHECK to see if the door and barrier are within a range
          while abs(door-barrier) < PATH_WIDTH:
               door = random.randint(2*PATH_WIDTH, lenghtOfTheWall-2*PATH_WIDTH)
          
          if(door<barrier):
               drawDoor()
               drawBarrier()
          else:
               drawBarrier()
               drawDoor()
          mazeDrawer.fd(lenghtOfTheWall)
          mazeDrawer.left(90)
          
#collision
endGame=Turtle()
endGame.goto(0,0)
endGame.shape("square")
endGame.color("Black")

#maze drawer speed/pen change
mazeDrawer.speed(0)
mazeDrawer.penup()

#more functions or commands
def lookUp():
     mazeDrawer.setheading(90)
def lookDown():
     mazeDrawer.setheading(270)
def lookRight():
     mazeDrawer.setheading(0)
def lookLeft():
     mazeDrawer.setheading(180)
def go():
     while True:
          mazeDrawer.fd(1)
          collision()
def speedchange():
     while True:
          mazeDrawer.fd(30) 
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10
def collision():
     if is_collided_with(mazeDrawer, endGame):
          print('Collision!')
          wn.bye()
          
#events and bindings
wn.onkeypress(lookUp,"Up")
wn.onkeypress(lookDown,"Down")
wn.onkeypress(lookLeft,"Left")
wn.onkeypress(lookRight,"Right")
wn.onkeypress(go,"g")
wn.onkeypress(go,"4")
wn.onkeypress(go,"space")
wn.onkeypress(speedchange,"s")

wn.listen()
wn.mainloop()