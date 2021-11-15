from Course import Course
from Student import Student
from Assignment import * #literally imports all functions and classes

cs = Course("Comp Sci")
math = Course("Easy Math")
lunch = Course("Lunch")
chem = Course("Chemistry 1")

stu1 = Student("bob","billy")
stu1.addcourse(cs)
stu1.addcourse(math)
stu1.addcourse(lunch)
stu1.addcourse(chem)

#staticmethod
#ClassName.method()

assignment1()
assignment2()