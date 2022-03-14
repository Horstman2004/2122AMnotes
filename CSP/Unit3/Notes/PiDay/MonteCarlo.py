import random
import math
import turtle as t
print("Insert number of points:")
np = input()
while not np.isdigit():
        print("Insert number of points:")
        np = input()
np = int(np)
t.speed("fastest")
length = 300 # radius of circle and length of the square in pixels
#draw y axis
t.pensize(2)
t.forward(length + 40)
t.left(135)
t.forward(20)
t.back(20)
t.left(90)
t.forward(20)
t.penup()
t.home()
t.pendown()

#draw x axis
t.left(90)
t.forward(length + 40)
t.left(135)
t.forward(20)
t.back(20)
t.left(90)
t.forward(20)
t.penup()
t.goto(0,length)
t.left(45)
t.left(180)
t.pendown()

#draw quarter circle
t.pencolor("red")
t.circle(length,-90)

inside = 0
for i in range(0,np):
        #get dot position
        x = random.uniform(0,length)
        y = random.uniform(0,length)
        #determine distance from center
        d = math.sqrt(x**2 + y**2)
        if d <= length:
                inside += 1
                t.pencolor("red")
        else:
                t.pencolor("blue")
        #draw dot
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot()

print(f"""
      Inside: {inside}
      Outside: {np}
      PI: {(inside/np)*4.0}
      
      
      """)




t.exitonclick()