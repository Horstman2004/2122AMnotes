import turtle as t
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']



donny = t.Turtle()
donny.shape("circle")
donny.up()
#draw 1 ow of red dots
y = 250

while y > -250:
    x=-250
    y-=50
    while x < 250:
        x+=50
        donny.goto(x,y)
        if x<=-200:
            donny.color("orange")
        else:
            donny.color("red")
        donny.stamp()
        donny.up()



wn = t.Screen()
wn.mainloop()