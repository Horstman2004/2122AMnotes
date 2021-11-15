import random

#pass in information
def giveMeSomeNumbers(ammountOfNumbers,smallest,biggest):
    listy=[]
    #create a list of 10 numbers
    for i in range(ammoutOfNumbers):
        listy.append(random.randint(smallest,biggest))
    print(listy)
    return listy

randomListOfNumbers=giveMeSomeNumbers(1000,82,495)
#randomListOfNumbers=giveMeSomeNumbers(10) missing arguments

print(min(randomListOfNumbers))
print(max(randomListOfNumbers))
print(sum(randomListOfNumbers))

#DO NOT -> REUSE or RENAME your funtions the same name as a built in function.
#define the function ave that takes in a list of numbers and returns the average
#def ave(listy):
    #return sum(listy)/len(listy)
#print(ave(randomListOfNumbers))

#range -> max value to th min value
#def range(listy):
    #return max(listy)-min(listy)

#print(range(randomListOfNumbers))



def isPrime(numbatocheck):
    #if it is divisible by itself or 1
    for i in range(2,numbatocheck):
        #check if numbertocheck is divisible to i
        if(numbertocheck%i==0):
            return False

    #if all calulations are not prime
    return True

for i in randonListOfNumbers:
    print(isPrime(i))
        print(True,i,randomListOfNumbers.index(i))