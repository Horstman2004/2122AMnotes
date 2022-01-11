import turtle as t
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

stamp = 0
stampcount=0

donny = t.Turtle()
donny.shape("square")
donny.up()
#draw 1 row of red dots

y = 200
rows=0
lengthtocheck=8
while y > -200:
    x=-200
    y-=50
    while x < 200:
        if stamp == lengthtocheck:
            x = -200
            y-=25
            rows+=1
            if rows%2 == 0:
                stamp+=1
                lengthtocheck=9
            else:
                lengthtocheck=8
        x+=60
        donny.goto(x,y)
        if stamp%2 == 0:
            donny.color("black")
        else:
            donny.color("red")   
        donny.stamp()
        stamp+=1      



wn = t.Screen()
wn.mainloop()