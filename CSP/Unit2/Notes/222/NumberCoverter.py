#1 byte = 8 bits = 256 unique integers = highest value is 256
decimal = int(input("Give me a pos whole number: "))

#1st find the ammount of bits
bitList=[]
exp = 0
while decimal>=16**exp:
    bitList.insert(0,16**exp) #change the exponent to change the base
    exp+=1
#print(bitList)

#2nd we itterated through the bits to find how many of eac bit is in our number
for i in range(len(bitList)):
    if decimal >= bitList[i]:
        decimal-=bitList[i]
        bitList[i] = "1"
    else:
        bitList[i] = "0"
    bitList = [int(item) for item in bitList]
print(bitList)


#3rd concatenated our 1's and 0's to output our string