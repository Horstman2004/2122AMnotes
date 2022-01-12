import turtle as t
import random
#iteration 1
"""
poly = 0

bob = t.Turtle()
bob.shape("turtle")
bob.forward(100)
bob.right(90)
bob.forward(100)
#bob.circle(100,180,10)
#bob.circle(100,180,5)

#using while loops to create shaps instead of for loops
while poly!=16:
        bob.forward(100)
        bob.left(90/4)
        poly+=1

window = t.Screen()
window.mainloop()
"""


#iteration 2
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']



'''
# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)  #sets direction
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.color("darkorchid")
painter.goto(20,190)
petals = 0

while (petals < 18):
        painter.right(20)
        painter.forward(30)
        painter.stamp()
        petals = petals + 1
        #if petals%2==0:
        #        painter.color("red")  
        #else:
        #        painter.color("darkorchid") 
        painter.color(random.choice(colors))
        
# ring 2 of flower
painter.goto(20,160)    # go to a certain spot on the canvas
painter.color("red")
petals = 0

while (petals < 12):
        painter.right(30)
        painter.forward(30)
        painter.stamp() #literally a stamp
        petals = petals + 1

painter.goto(10,130)    # go to a certain spot on the canvas
painter.color("red")
petals = 0

while (petals < 888888):
        painter.right(50)
        painter.forward(25)
        painter.stamp() #literally a stamp
        petals = petals + 1
        painter.forward(2)

wn = t.Screen()
wn.mainloop()
'''

#iteration 3

painter = t.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

def randoColor():
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=random.randint(0,255)
     return r,g,b      #return a tuple of rgb

t.colormode(255) #to allow the color to take RGB
# draw flower
painter.color("blue")
painter.goto(20,180)
petals = 0

while True:
        painter.color(random.choice(colors))
        painter.goto(20,180)
        petals = 0


        while (petals < 18):
                if petals%3==0:
                        painter.color(randoColor())     
                elif petals%3==1:
                        painter.color(randoColor())
                else:
                        painter.color(randoColor())
        painter.right(20)
        painter.forward(30)
        painter.stamp()  #is literally a stamp
        petals = petals + 1
        painter.goto(20,150)        #CHANGED
        petals = 0


        while (petals < 12):        #CHANGED
                if petals%3==0:
                        painter.color(randoColor())     
                elif petals%3==1:
                        painter.color(randoColor())
                else:
                        painter.color(randoColor())
        painter.right(30)        #CHANGED
        painter.forward(30)
        painter.stamp()
        petals = petals + 1
        painter.goto(20,120)        #CHANGED
        petals = 0


        while (petals < 6):        #CHANGED
                if petals%3==0:
                        painter.color(randoColor())     
                elif petals%3==1:
                        painter.color(randoColor())
                else:
                        painter.color(randoColor())
        painter.right(60)        #CHANGED
        painter.forward(30)
        painter.stamp()
        petals = petals + 1

        painter.goto(12,90)
        painter.color(randoColor())
        painter.stamp()
        wn = t.Screen()
        wn.mainloop()