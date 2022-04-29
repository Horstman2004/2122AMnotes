#imports
import turtle
import time

#screen
root = turtle.Screen()

#Constants
RADIUS = 300
WEDGES = 8
DEGREE_ANGLE= 360/WEDGES
TOTAL_DEGREE=360

#Lists
colors="red"
turtles=[]

#turtle
turt = turtle
turt.hideturtle()
turt.pendown()
turt.speed(0)
turt.sety(turtle.ycor() - RADIUS)
turt.showturtle()

#making list of 8 different turtles

def coolCircle(): 
    for j in range(8):
        turt.circle(RADIUS,DEGREE_ANGLE)
        turt.setheading((WEDGES-(j+1))*DEGREE_ANGLE)
        turt.forward(150)
    root.update()


coolCircle()

root.mainloop()