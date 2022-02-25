from turtle import Screen, Turtle
from colorsys import hsv_to_rgb

RADIUS = 300
NUMBER_OF_WEDGES = 28
SLICE_ANGLE = 360 / NUMBER_OF_WEDGES

screen = Screen()
screen.tracer(False)

# create a pie wedge-shaped cursor
turtle = Turtle(visible=False)
turtle.begin_poly()
turtle.sety(turtle.ycor() - RADIUS)
turtle.circle(RADIUS, extent=SLICE_ANGLE)
turtle.home()
turtle.end_poly()

screen.register_shape("wedge", turtle.get_poly())

# create a turtle for each wedge in the pie
turtles = []

for hue in range(NUMBER_OF_WEDGES):
    turtle = Turtle("wedge")
    turtle.color(hsv_to_rgb(hue / NUMBER_OF_WEDGES, 1.0, 1.0))
    turtle.setheading(hue * SLICE_ANGLE)

    turtles.append(turtle)

def draw_circle():

    # have each turtle take on the color of its neighbor
    for index, turtle in enumerate(turtles):
        turtle.color(*turtles[(index + 1) % NUMBER_OF_WEDGES].color())

    screen.update()
    screen.ontimer(draw_circle, 80)

draw_circle()

screen.exitonclick()