import turtle as t
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

stamp = 0
stampcount=0

donny = t.Turtle()
donny.shape("square")
donny.up()
#draw 1 ow of red dots
y = 200

while y > -200:
    x=-200
    y-=50
    while x < 250:
        x+=60
        donny.goto(x,y)
        if stamp%2 == 0:
            donny.color("black")
        elif stamp%2 == 1:
            donny.color("red")
        elif stampcount == 8:
            stamp+=2     
        donny.stamp()
        stamp+=1      
        donny.up()



wn = t.Screen()
wn.mainloop()