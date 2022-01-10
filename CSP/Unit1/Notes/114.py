#print out 0 -99
#for i in range(10000): 
    #for c in range(10000): 
        #print ((str(i))+(str(c)),end=" ")
    
i=0   
while i < 10000:
    
    c=0
    while c < 10000:
        print(str(i)+str(c))
        c+=1
    i+=1
    print()