#python3 uses tkinter / python2 uses tkinter
from tkinter import *

masterUsername = "admin"
masterPassword = "admin"

def pressMyButton():
    print("You have pressed my button")
    #get the info from the GUI
    un = usernameEntry.get()
    pw = passwordEntry.get()       #get the info from the GUI 
    
    #check it against the master log in
    if un == masterPassword and pw == masterPassword:
        print("You're logged in")
        authFrame.tkraise()
        
def logoutButtonPressed():
    print("Logout Pressed")
    loginFrame.tkraise()

#in turtle: wn=Screen()
root = Tk()                 #creates your screen
root.title("Login System")         #set window title
root.wm_geometry("400x300") #size of the window

#Frame for the login
#object = COnstructor(window)
authFrame = Frame(root)
authFrame.grid(row=0,column=0,sticky='news')

loginFrame = Frame(root)
loginFrame.grid(row=0,column=0,sticky='news')
#sticky is an anchor parameter to the north east west south

#items into the frame
#hungarian naming convention
usernameLBL = Label(loginFrame,text="Username: ")
usernameLBL.pack(pady=5,padx=5)
usernameEntry = Entry(loginFrame, bd=3)
usernameEntry.pack(pady=5)
passwordLBL = Label(loginFrame,text="Password: ")
passwordLBL.pack(pady=5,padx=5)
passwordEntry = Entry(loginFrame, bd=3, show="*")
passwordEntry.pack(pady=5)

loginBTN = Button(loginFrame,text="Login",command=pressMyButton)
loginBTN.pack(pady=20,padx=175)

logoutBTN = Button(authFrame,text="Logout",command=logoutButtonPressed)
logoutBTN.pack(pady=20,padx=175)

root.mainloop()

