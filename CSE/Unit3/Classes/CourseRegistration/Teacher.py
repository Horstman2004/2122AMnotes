class Teacher:
    
    teacherID = 0
    
    #intiialization -> constructor
    def __init__(self,firstName,lastName):
        self.first = firstName
        self.last = lastName
        self.courses = []   #each teacher has their own list
        self.teacherID = Teacher.teacherID 
        Teacher.teacherID+=1
        
        #toString method
    def __str__(self):
        out = ""
        out = f"{self.teacherID} {self.last}, {self.first}\n"
        for course in self.courses:
            out+=f"\t{course}\n"  #every loop, course becomes the next course in the list
        
        return self.courses
    
    #set the name
    def setName(self,newFirst,newLast):
        self.first = newFirst
        self.last = newLast
    
    #get the id
    def getteacherID(self):
        return self.teacherID
    
    #add a course
    def addcourse(self,newCourse):
        self.courses.append(newCourse)