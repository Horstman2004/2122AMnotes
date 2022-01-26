import turtle as t


COURT_HEIGHT = 600
COURT_WIDTH = 1000

wn = t.Screen()

border = t.Turtle(visible=False)    #same as hideturtle

def draw_field():
    wn.bgcolor("gray")
    border.speed(0)
    border.pensize(3)
    border.penup()
    border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.penup()
    border.sety(-COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_WIDTH)
    border.penup()
    border.setposition(0,-COURT_HEIGHT/2)
    border.pendown()
    border.setheading(90)
    border.pensize(1)
    for i in range(COURT_HEIGHT//50):   #// returns int value for range
        border.forward(26)
        border.penup()
        border.forward(26)
        border.pendown()
    
draw_field()


wn.mainloop()