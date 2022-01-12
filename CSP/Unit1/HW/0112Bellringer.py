import turtle as t

t.setup(500,500)
t.width(10)
t.penup()
t.left(90)
t.goto(-240,-230)
t.pendown()
t.forward(500)
t.penup()
t.goto(240,-230)
t.pendown()
t.forward(500)
t.penup()
t.goto(0,-500)
x=0
y=-230
t.color("yellow")
for i in range(8):
    t.goto(x,y)
    t.pendown()
    t.forward(30)
    t.penup()
    y+=75
    





wn = t.Screen()
wn.mainloop()




