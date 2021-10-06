#conditionals are based on boolean statements
print(type(5)) #integer
print(type("true")) #string - look for quotes
print(type(0)) #boolean
#True and False are built into python

#Converting Functions
#int() -> convert anything to an int if possilbe
#str()
#float()
#bin()
#bool() - Convert anything to a boolean statement IF POSSIBLE

print(bool(1)) #prints out true
print(bool(0)) #prints out false
print(bool(50)) #if it isn't 0 - - > It's true
print(bool(-3.82)) #True


x = 4
#if something is true:
if x==4:
#   then do this
    print("correct")
#if something else is true:
elif x>4:
#   then do that
    print("to high")
#all else fails:
else:
#   then do this
    print("to low")

if x<4:
    print("hi")
elif x>4:
    print("hi")
    if x<10:
        print("hi")
    else:
        print("hi")



#ask the user if they had breakfast
#   if they did, ask them what they ate

food = input("Did you have breakfast today? ")

if food == "yes":
    input("What are you eating? ")
elif food == "no":
    input("What would you like for breakfast? ")
else:
    ("Sorry I didn't understand you.")


'''
    Relational Operators
        ==  equal to
        <=  less than equal to
        >=  greater than or equal to
        !=  not equal to
        not the opisite of the next boolean expression
        and means both sides have to be true
        or means one of the sides has to be true
'''

x=input("what is your x value ")
y=input("what is your y value ")
if x>=0:
    if y>=0:
        if x<=50:
            if y<=50:
                print("youre in the box")
else:
    print("you're not in the box")

if x>=0 and y>=0 and x<=50 and y<=50:
    print("in")
else:
    print("out")


