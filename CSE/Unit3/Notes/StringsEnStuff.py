"""
print("StringMainpulation")
'''
    Data  Types
        Int, Float, Strings, List, Booleans
        Primitive: Int, Booleans, Float
        Non-Primitive: Strings, List 
'''

#String Math
name="bobby"
age=17
print("Hello" + "Bobby") #String addition / concatenation
print("Hello" + name) #string addition
print("Your age is "+str(age))     #concatenation 

#convert a string ti an int
print(int("17"))

#convert an Int. or anything to a string
print(str(age))

name=input("Your name: ")
grade=input("Grade level: ")
print("Wow, "+name+" you're in the "+ str(grade)+" grade")


pet=input("What is your pets name?")
age=input("How old is your pet?")
size=input("How big is your pet?")
smell=input("Does your pet smell good?")

print("Your pet is a "+pet+" sounds like a cool pet. I can't believe they are that"+age+" and that "+size+".")
print("I like "+smell+"smelling pets")

#convert your name to binary
print(bin(72))      #needs and int
#built in function: print, input, str, int, bin
#convert a character to an int
print(ord("B"))     #returns it
print(bin(ord("b")))        #convert youru name to binary
print(bin(ord("a"))) 
print(bin(ord("n"))) 
print(bin(ord("d"))) 
print(bin(ord("e"))) 
print(bin(ord("r"))) 

print(bin(16))
print(bin(-16))
print(bin(0))



'''
    Ask the user for how much gas costs
    Ask the user for how many gallons they purchased
    Output the total coast of the fill up
'''
cost=input("gas cost")
gal=input("num of gallons")
#convert string to float
total=float(cost)*int(gal)
print(total)


print("poop"+"poop") #add strings
print("poop"*20) #multiply strings
#print("poopie"-"ie") #subtract strings doesn't work
#print("poop"/3) dividing strings doesn't work
"""