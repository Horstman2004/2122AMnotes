sandwich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3
keepordering=True
orderMasterList=[]
runningTotalPrintOut=""
tax = .07
total=0
     
while(keepordering):
    
    
    #Ordering Burger
    orderInformation = "\nYour Order:\n"
    chooseSandwich,chooseFries,chooseDrink = False,False,False
    order = ["", "", "", 0]     
    krabbypatty = input("Would you like a krabby Patty or a Krabby Meal? (y,n,meal)")
    if krabbypatty == "y":
        krabbypatty = input("How many patties would you like?:   ($1.25 Single, $2.00 Double, $5.75 Triple) ")
        if krabbypatty=="S" or krabbypatty=="D" or krabbypatty=="T" or krabbypatty=="S/C" or krabbypatty=="D/C" or krabbypatty=="T/C":  #with or without sea cheese options
            orderInformation+=(f"\tKrabby Patty:\t{krabbypatty}\n")
            order[sandwich_index]=krabbypatty   #replace whatever is in the order list
            chooseSandwich=True
        if krabbypatty == "S":
            total+=1.25
        elif krabbypatty == "D":
            total+=2.00
        elif krabbypatty == "T":   
            total+=3.00
        elif krabbypatty == "S/C":
            total+=1.50
        elif krabbypatty == "D/C":
            total+=2.25
        elif krabbypatty == "T/C":
            total+=3.25
            
    elif krabbypatty == "n":
        orderMasterList.append("no burger")
    elif krabbypatty == "meal":
        #Ordering Meal/Combo
        krabbypatty = input("What size meal would you like?:   ($3.50 Small, $3.75 Medium, $4.00 Large) ")  #asking for meal size
        if krabbypatty=="S" or krabbypatty=="M" or krabbypatty=="L":
            orderInformation+=(f"\tKrabby Patty:\t{krabbypatty}\n")
            order = ["", "", "", 0] 
            order[sandwich_index]=krabbypatty   #replace whatever is in the order list
            chooseSandwich=True
        if krabbypatty == "S":
            total+=3.50
        elif krabbypatty == "M":
            total+=3.75
        elif krabbypatty == "L":    
            total+=4.00
    
    
    '''
    #Ordering Other Meals
    orderInformation = "\nYour Order:\n"
    chooseSandwich,chooseFries,chooseDrink = False,False,False
    order = ["", "", "", 0]     
    krabbypatty = input("Would you like a krabby Patty or a Krabby Meal? (y,n,meal)")
    '''
    
    
    #Ordering Beverage
    drink = input("Would you like a drink? (y,n) ")
    if drink == "y":
        chooseDrink=True
        drink = input("What drink would you like? Seafoam Soda or Kelp Shake? (ss,ks)")
        if drink == "ss":
            drink == input("What size would you like? (s,m,l)")
            if drink == "s":
                total+=1
                drink="Small Seafoam Soda"
            elif drink == "m": 
                total+=1.25
                drink="Medium Seafoam Soda"
            elif drink == "l":
                total+=1.5
                drink="Large Seafoam Soda"
        elif drink=="ks":
                total+=2
                drink="Kelp Shake"
    elif drink == "n":
        orderMasterList.append("No Drink")

        orderInformation+=(f"\tDrink:\t\t{drink}\n")
        order[beverage_index]=drink   #replace whatever is in the order list
    
    
    
    #Coral Bits/Kelp Rings
    fries = input("Would you like fries with that? (y,n) ")
    if fries == "y":
        chooseFries=True
        fries = input("Which size? s,m,l ")
        if fries == "s":
            fries = input("Would you like to Mega-Size? (y,n) ")
            if fries=="y":
                fries="l"
                total+=2.00
            else:
                fries="s"
                total+=1.00
        elif fries == "m":
            total+=1.75
        elif fries == "l":
            total+=2.00
    elif fries == "n":
        orderMasterList.append("no fries")
        orderInformation+=(f"\tSide:\t\t{fries}\n")
        order[fries_index]=fries   #replace whatever is in the order list



    #Salty Sauce
    saltysauce = int(input("How many salty sauce packets do you want? ($.25 ea) "))
    total+= (saltysauce*.5)
    orderInformation+=(f"\tSalty Sauce:\t{saltysauce}\n")
    order[sandwich_index]=saltysauce   #replace whatever is in the order list
    orderInformation+=(f"\tSubtotal: $\t{total}\n")
    
    
    # print(orderInformation)

    orderPrintOut = (f'''
    Your order:
        Sandwich:  {krabbypatty}
        Drink:     {order[1]}
        Side:         {order[2]}
        Salty Sauce:  {order[3]}
        Subtotal: ${total}
        Final Total: ${total}
    ​
    ''')

    orderMasterList.append(order)
    runningTotalPrintOut += orderPrintOut
    

    if (input("Do you want another order? (y/n)")=="n"):
        keepordering=False
        
        
print(orderMasterList)
print(runningTotalPrintOut)