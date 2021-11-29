from Course import Course

math = Course("Math")
science = Course("Science")
history = Course("History")

while(ui == " "):
    ui =  input("What course are you looking to find?")
    if ui == "math":
        print("I've found, Math.")
    elif ui == "science":
        print("I've found, Science")
    elif ui == "history":
        print("I've found, History")
    else: 
        print("Course not found. Please try again.")
    

    
    