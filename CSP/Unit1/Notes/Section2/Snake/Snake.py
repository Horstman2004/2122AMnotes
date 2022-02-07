#import
from tkinter import font
import turtle as t
import time
import random

#game configuration
delay = 0.1
bodyParts=[]
snakeSpeed = 5
starter=False

#starter functions

#create turtle objects
wn = t.Screen()
wn.bgcolor("pink")
wn.setup(width=600,height=600)        #give a default screen size

#mainloop

head = t.Turtle(shape="square")
head.speed(snakeSpeed)
head.penup()
head.direction="stop"

#create the food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)    #scaling the food down by 50%
food.color("green")
food.penup()
food.goto(100,100)

food1 = t.Turtle()
food1.speed(0)
food1.shape("circle")
food1.shapesize(.5,.5)    #scaling the food down by 50%
food1.color("green")
food1.penup()
food1.goto(-40,170)

food2 = t.Turtle()
food2.speed(0)
food2.shape("circle")
food2.shapesize(.5,.5)    #scaling the food down by 50%
food2.color("green")
food2.penup()
food2.goto(90,-100)
#function 
def up():
    if head.direction != "down":
        head.direction="up"  
def down():
    if head.direction != "up":
        head.direction="down"   
def left():
    if head.direction!="right":
        head.direction="left"      
def right():
    if head.direction!="left":
        head.direction="right"
def move():
    #depending on the direction, the coordinates change
    if head.direction == "up":
        y = head.ycor()     #get the y coordinate
        head.sety(y+20)     #set the new y coordinate
        
    elif head.direction == "down":
        y = head.ycor()     #get the y coor
        head.sety(y-20)     #set the new y coordinate
    
    elif head.direction == "right":
        x = head.xcor()     #get the x coor
        head.setx(x+20)     #set the new x coordinate
    
    elif head.direction == "left":
        x = head.xcor()     #get the x coor
        head.setx(x-20)     #set the new x coordinate
        
def hideTheBodyParts():       #gameover
    global bodyParts
    time.sleep(1)            #wait a second
    head.goto(0,0)
    head.direction="stop"
    #hide the parts
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts=[]
    
def speed():
    global snakeSpeed
    snakeSpeed+1
    head.speed(snakeSpeed)
        
#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")

#main game loop
while True:
    wn.update()    #updates or refreshes the screen

    #Border Collision?
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        hideTheBodyParts()

    #Food Collision?
    #if head and food's distance < 20
    # turtle.distance(turtle) -> distance between 2 turtle obj
    if head.distance(food) < 20:
        #move the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(snakeSpeed)
        part.shape("square")
        part.color("gray")
        part.penup()
        bodyParts.append(part)
        speed()
    if head.distance(food1) < 20:
        #move the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food1.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(snakeSpeed)
        part.shape("square")
        part.color("gray")
        part.penup()
        bodyParts.append(part)
        speed()
    if head.distance(food2) < 20:
        #move the food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food2.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(snakeSpeed)
        part.shape("square")
        part.color("gray")
        part.penup()
        bodyParts.append(part)
        speed()

    #move the snake
    #Move the butt to the neck
    for i in range(len(bodyParts)-1, 0, -1):    #last index to the first index
        x=bodyParts[i-1].xcor()  #get the x of the next bodypart
        y=bodyParts[i-1].ycor()  #get the y of the next bodypart
        bodyParts[i].goto(x,y)   #reset the current bodypart x,y

    #Move the neck to the head
    if len(bodyParts)>0:
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y)
        move()    #Move the head

    #Did we hit ourselves?
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()

    time.sleep(delay)