#imports
from turtle import *
import random

#barrier UI
distance = 500
PATH_WIDTH = 20
NUMWALLS = 25
collision = False
randNumList = []

wn=Screen()
mazeDrawer = Turtle()
mazeDrawer.penup()
mazeDrawer.goto(100,-100)
mazeDrawer.pendown()
mazeDrawer.speed(0)
mazeDrawer.pensize(5)
mazeDrawer.setheading(90)

#ghosts
ghost1 = Turtle()
ghost2 = Turtle()
ghost3 = Turtle()

ghost1.speed(1)
ghost2.speed(1)
ghost3.speed(1)

ghost1.penup()
ghost2.penup()
ghost3.penup()

ghost1.shapesize(2)
ghost2.shapesize(2)
ghost3.shapesize(2)

ghost1.shape("turtle")
ghost2.shape("turtle")
ghost3.shape("turtle")

ghost1.color("red")
ghost2.color("red")
ghost3.color("red")

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

#Speed Change Button

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
          mazeDrawer.forward(lenghtOfTheWall)
          mazeDrawer.left(90)
          
for i in range(15):
     randNumList.append(random.randint(-200,200))
print(randNumList)
#collision
endGame=Turtle()
endGame.goto(-10,0)
endGame.shape("square")
endGame.color("white")
endGame.shapesize(8)

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
          mazeDrawer.forward(1)
          collision()

def speedchange():
     while True:
          mazeDrawer.forward(30) 

#collision functions
def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

def collisionT():
     global collision
     if is_collided_with(mazeDrawer, endGame):
          collison = True
          print('Collision!')
          wn.bye()

#ghost movement
def ghostMovement1():     #movement for ghosts
     global collision
     if collision != True:
          ghost1.forward(32)
          ghost1.setheading(random.choice(randNumList))
          
def ghostMovement2():     #movement for ghosts
     global collision
     if collision != True:
          ghost2.forward(17)
          ghost2.setheading(random.choice(randNumList))
          
def ghostMovement3():     #movement for ghosts
     global collision
     if collision != True:
          ghost3.forward(23)
          ghost3.setheading(random.choice(randNumList))
          
while collision != True:
     ghostMovement1()
     ghostMovement2()
     ghostMovement3()

#events and bindings
wn.onkeypress(lookUp,"w")
wn.onkeypress(lookDown,"s")
wn.onkeypress(lookLeft,"a")
wn.onkeypress(lookRight,"d")
wn.onkeypress(go,"g")
wn.onkeypress(speedchange,"r")

wn.listen()
wn.mainloop()