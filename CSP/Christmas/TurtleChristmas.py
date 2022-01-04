#x.y is jn the middle
from turtle import *

myPen = Turtle()
window = Screen()

while True:
    for i in range(4):
        myPen.right(90)
        myPen.forward(100)

myPen.penup()
myPen.goto(-200,-200)
myPen.pendown()

for i in range (4):
    myPen.right(90)
    myPen.forward(100)

myPen.circle(60)
myPen.forward(100)
myPen.left(135)
myPen.forward(100/1.4)







mainloop()