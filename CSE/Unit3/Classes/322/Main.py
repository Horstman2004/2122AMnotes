#from the file import class
from Post import Post

post1=Post("bob","hello")   #runs the __init__ function

#post 1 is an object


#objects can hold multiple varibles and have methods
#varibles and store data
username="bob"
message="hello"

print(post1.un)
print(post1.msg)

username="sally"
message="howdy"
post2=Post("sally","howdy")

print(post2.un,post2.msg)


#printing the post
print(post1)                #runs the __str__ function