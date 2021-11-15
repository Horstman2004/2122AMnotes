'''
    Procedures - Purple blocks
    Functions - Block of code that completes an algorithm
    Methods - Methods are used with objects and Classes

    Two mains types of funtions:
    void (to do) - it doesn't return anything
    return (the ruesults) - it gives the computer data back


#define a funtion called howdy
def howdy():
    #print out howdy
    print("howdy")

#call the print function
print("the message to print")
#call the howdy function
howdy()

#define a function that adds 2 numbers together
def adding():
    a=int(input("give me a number"))
    b=int(input("give me a number"))
    print(a+b)

adding()

#define a function ymxb
def ymxb(): 
    #solve for y in the y=mx+b formula
    m=int(input("m: "))
    x=int(input("x: "))
    b=int(input("b: "))
    print(m*x+b)
'''

def ymxb(m,x,b): 
    #solve for y in the y=mx+b formula
    print(m*x+b)

#return something
def returnYMXB(m,x,b)
    return (m*x+b)

print("x | y")
print("-----")
for i in range(101): 
    #place in the 3 arguments   
    #print(returnymxb(3,i,-2))    #i is the x value for this equation
    print(f"{i} | {returnYMXB(3,i,-2)}")
