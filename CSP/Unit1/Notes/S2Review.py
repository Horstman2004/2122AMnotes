'''
#loops...
#for loop
#loop through a string and print out each letter
s = "elephant"
#for each loop
for letter in s:
    print(letter)
print()
#traditional fro loop
for i in range(len(s)):
    print(s[i])
sL=list("elephant")
print(sL)
#find the index of p
for i in range(len(sL)):
    if sL[i] == "t":
        #print index
        sL[i]="y"
print(str(''.join(sL))) 

def listToString(listy):
    out=""
    for eachLetter in listy:
        out += eachLetter
    print(out)
listToString(sL)
'''

s = "seahorse"
#print the index of the vowels - try using a while loop
vowelsList="aeiou"
i=0
while i<len(s):
    if s[i] in vowelsList:
        print(i)
    i+=1
    