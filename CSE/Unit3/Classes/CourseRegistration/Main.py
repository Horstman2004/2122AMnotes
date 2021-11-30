from Course import Course
from Student import Student
from Teacher import Teacher
from Assignment import * #literally imports all functions and classes

teacherList=[Teacher("Billy","Susan"),Teacher("Billy2","Susan2"),Teacher("Billy3","Susan3")]
courseList=[Course("Lunch",teacherList[0]),Course("Algebra",teacherList[1]),Course("Anatomy",teacherList[2])]
studentList=[]

classToLookup = "Algebra"
#for course in courseList:
    #if course.name == "Lunch":
        #print(Course.courseID,Course.name,Course.teacher)


with open("data/teacher.csv","r") as file:
    teacherFile = file.readlines()
    
for line in teacherFile:
    name,course,junk = line.split("\t",2)
    print(name,course)

    teacherList.append(Teacher(name,course))
i=-1  
for line in teacherFile:
    nameOfTeacher,nameOfCourse,junk = line.split("\t",2)
    if i!=2:
        courseList.append(Course(nameOfCourse,teacherList[i]))
    i+=1
        

print(teacherList)


print(teacherFile)
    












first=""
last=""
newStudent=""

while newStudent=="y":
    first=input("Students First: ")
    last=input("Students Last: ")
    studentList.append(Student(first,last))
    
    newStudent = input("Do you have a new student? (y,n)")
    
    
for student in studentList: 
    print(studentList)
