import turtle as t
t.bgcolor("gray")
t.color("white")
t.setup(1280,720)
t.width(5)
t.penup()
t.goto(-200,100)
t.setheading(45)
t.pendown()
t.forward(25)
t.setheading(90)
t.forward(200)
t.goto(-200,500)
t.setheading(45)
t.pendown()
t.forward(25)
t.setheading(90)
t.forward(200)
x=0
y=-230
t.color("gray")
for i in range(3):
    t.goto(x,y)
    t.pendown()
    t.forward(30)
    t.penup()
    y+=75






wn = t.Screen()
wn.mainloop()