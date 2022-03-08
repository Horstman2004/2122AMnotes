#1 byte = 8 bits = 256 unique integers = highest value is 256


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
dec2hex(1047)