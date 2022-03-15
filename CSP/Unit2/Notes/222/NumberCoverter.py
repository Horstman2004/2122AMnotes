#1 byte = 8 bits = 256 unique integers = highest value is 256


from functools import reduce


def dec2bin(decimal):
    #1st find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=1**exp:
        digitList.insert(0,1**exp) #change the exponent to change the base
        exp+=1
    print(digitList)

    #2nd we itterated through the bits to find how many of eac bit is in our number
    for i in range(len(digitList)):
        if decimal >= digitList[i]:
            decimal-=digitList[i]
            digitList[i] = "1"
        else:
            digitList[i] = "0"
        digitList = [int(item) for item in digitList]
    print(digitList)

def dec2hex(decimal):
    #1st find the ammount of bits
    digitList=[]
    exp = 0
    while decimal>=16**exp:
        digitList.insert(0,16**exp) #change the exponent to change the base
        exp+=1
    print(digitList)

    #2nd we itterated through the bits to find how many of eac bit is in our number
    for i in range(len(digitList)):
        temp=digitList[i]
        digitList[i]=decimal//digitList[i]
        decimal-=(digitList[i]*temp)
    #3rd concatenated our 1's and 0's to output our string
    #4th Concate the digitList together
    out="0x"
    for b in digitList:
        out+=str(b)
    print(out)

def hex2dec(hex):
    #help from https://stackoverflow.com/questions/19376202/converting-hexadecimal-to-decimal-in-python
    conversiontable = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    hexlist = list(hex)
    for i, num in enumerate(hexlist):            #enumerate yields pairs
        num = num.upper()
        if num in conversiontable:               #if num(letter) is in the list it will remove that letter and append a number
            hexlist[i] = conversiontable[num]
    intlist = [int(num) for num in hexlist]
    sum = reduce(lambda x, y: x*16+y, intlist)
    print(sum)

def octButton(decimal):
    digitList=[]
    exp = 0
    while decimal>=8**exp:
        digitList.insert(0,8**exp) #change the exponent to change the base
        exp+=1
    print(digitList)
    
    for i in range(len(digitList)):
        temp=decimal//digitList[0]
        digitList 
        
        print(digitList)
    
    
    """octList = [decimal]
    for i in range(len(decimal)):
        if decimal > 8:
            remain = decimal%8
            decimal = remain
            octList.append(remain)
        else:
            remain = decimal/8
            octList.append(remain)
        print(octList)"""


#https://stackoverflow.com/questions/35450560/how-to-use-python-to-convert-an-octal-to-a-decimal
#-----------------------------------------------------------------------------------------------
def dec2base():
    a = int(input('Enter decimal number: \t'))
    d = int(input('Enter expected base: \t'))
    b = ""
    while a != 0:
        x = '0123456789ABCDEF'
        c = a % d
        c1 = x[c]
        b = str(c1) + b
        a = int(a // d)
    print(b)

def todec(base,digit):
    digitList = list(digit)
    outputNum = 0
    conversionList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for exp, digit in enumerate(digitList[-1::-1]):
        conversionDigit = conversionList.index(digit)
        if int(conversionDigit)/base >= 1:
            print('Error')
            break
        outputNum = (int(conversionDigit) * (base**exp)) + outputNum
    print(outputNum)
todec(16,"417")

#-----------------------------------------------------------------------------------------------