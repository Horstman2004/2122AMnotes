import turtle as t

t.setup(500,500)
t.width(10)
t.penup()
t.left(90)
t.goto(-230,-250)
t.pendown()
t.forward(20)
t.penup()
t.goto(50,-50)
t.pendown()
t.forward(50)
t.penup()
t.goto(0,-50)
x=0
y=-230
t.color("yellow")
for i in range(3):
    t.goto(x,y)
    t.pendown()
    t.forward(30)
    t.penup()
    y+=75






wn = t.Screen()
wn.mainloop()