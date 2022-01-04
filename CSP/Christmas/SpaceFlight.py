from tkinter import *
import random

root = Tk()
canvas = Canvas(root,height=600,width=600,bg="black")
canvas.grid()
canvas.create_text(300,100,text="Hello Space",fill="white",font=32)

from PIL import ImageTK, Image
#open a picture
imgFile - Image.open("Falcon.png")
imgFile = imagFile.resize((100,100))
#convert it to a TkPicture
imgTK = ImageTk.PhotoImage(imgFile)
#render the TKpicture
img = canvas.create_image(300,300,image=imgTK)

stars=[]
for i in range(100):
    centerX = random.randint(0,600)
    centerY = random.randint(0,600)
    canvas.create_rectangle(centerX-2,centerY-2,centerX+2,centerY+2,fill="yellow")
print(stars)

def animate():
    for s in range(len(stars)):
        x1,y1,x2,y2 = canvas.coords(stars[s])
        canvas.coords(stars[s], x1, 0, x2, 4)
        if y2 > 600:
            canvas.coords(stars[s], x1, 0, x2, 4)
    canvas.after(1,animate)

root.mainloop()