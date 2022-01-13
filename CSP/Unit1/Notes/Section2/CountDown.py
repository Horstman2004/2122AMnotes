import turtle as t 

timer=5
timesUp=False
counterInterval = 1000
fontSetup=("Comic Sans MS", 30, "normal")


wn = t.Screen()
counter = t.Turtle()

def countdown():
    global timer, timesUp
    counter.clear()
    if timer<=0:
        counter.write("Times Up!",font=fontSetup)
        timesUp=True
    else:
        counter.write(f'Time: {timer},font=fontSetup')
        timer-=1
    print(timer)

#wn.onscreenclick()     Run a command when the screen is clicked
counter.getscreen().ontimer(countdown,counterInterval)
#.ontimer(command,interval)
wn.ontimer(countdown,counterInterval)     #"acts" like the clock widget from MIT

wn.mainloop()