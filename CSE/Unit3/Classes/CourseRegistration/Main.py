from Course import Course
from Student import Student
from Teacher import Teacher
from Assignment import * #literally imports all functions and classes

teacherList=[Teacher("Billy","Susan"),Teacher("Billy2","Susan2"),Teacher("Billy3","Susan3")]
courseList=[Course("Lunch",teacherList[0]),Course("Algebra",teacherList[1]),Course("Anatomy",teacherList[2])]
studentList=[]

classToLookup = "Algebra"
for course in courseList:
    if course.name == "Lunch":
        print(Course.courseID,Course.name,Course.teacher)



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
