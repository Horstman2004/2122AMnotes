#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5
game = True

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()


maze1 = False
maze2 = True
maze3 = False
#---- TODO: change maze here
while game == True:
  wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png
  
  
  #---- TODO: begin robot movement here
  while maze2 == True:
    i=0
    while i<5:
      move()
      i=i+1
      if i == 3:
        turn_left()
        turn_left()
        turn_left()
      elif i >= 5:
        maze2 = False
        maze3 = True
        break
'''
  #mazepng1
  while maze1 == True:
    i=0
    while i<8:
      move()
      i=i+1
      if i == 4:
        turn_left()
        turn_left()
        turn_left()
      elif i >= 8:
        maze1 = False
        maze2 = True
        break
'''
  


#mazepng2

# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
i = 0
while (i < 3): # forward 3
  move()
  i = i + 1 
'''

#---- end robot movement 

wn.mainloop()
