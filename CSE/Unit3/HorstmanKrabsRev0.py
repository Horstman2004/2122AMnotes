sandwich_index = 0
other_index = 1
beverage_index = 2
fries_index = 3
salty_index = 4
keepordering=True
orderMasterList=[]
runningTotalPrintOut=""
tax = .07
total = 0
     
while(keepordering):
    
    
    #Ordering Burger 
    krabbypatty = input(f'''Would you like a krabby Patty or a Krabby Meal?
    Yes = y
    No = n
    Meal = m
    ''')
    if krabbypatty == "y":
        krabbypatty = input(f'''How many patties would you like?:   
        $1.25 Single 
        $2.00 Double 
        $5.75 Triple 
        s = Single d = Double t = Triple
        s/c = Single with Cheese
        m/c = Medium with Cheese
        l/c = Large with Cheese''')
        orderInformation = "\nYour Order:\n"
        chooseSandwich,chooseFries,chooseDrink = False,False,False
        order = ["", "", "", 0]     
        orderInformation+=(f"\tKrabby Patty:\t{krabbypatty}\n")
        order[sandwich_index]=krabbypatty   #replace whatever is in the order list
        chooseSandwich=True
        if krabbypatty == "s":
            total+=1.25
            krabbypatty = "Single"
        elif krabbypatty == "d":
            total+=2
            krabbypatty = "Double"
        elif krabbypatty == "t":   
            total+=3
            krabbypatty = "Triple"
        elif krabbypatty == "s/c":
            total+=1.5
            krabbypatty = "Single w/ Cheese"
        elif krabbypatty == "d/c":
            total+=2.25
            krabbypatty = "Double w/ Cheese"
        elif krabbypatty == "t/c":
            total+=3.25
            krabbypatty = "Triple w/ Cheese"
    elif krabbypatty == "m":
        #Ordering Meal/Combo
        krabbypatty = input(f'''What size meal would you like?  
        $3.50 Small = s
        $3.75 Medium = m
        $4.00 Large = l
    ''')  #asking for meal size
        if krabbypatty=="S" or krabbypatty=="M" or krabbypatty=="L":
            orderInformation+=(f"\tKrabby Patty:\t{krabbypatty}\n")
            order = ["", "", "", 0] 
            order[sandwich_index]=krabbypatty   #replace whatever is in the order list
            chooseSandwich=True
        if krabbypatty == "s":
            total+=3.5
            krabbypatty = "Small"
        elif krabbypatty == "m":
            total+=3.75
            krabbypatty = "Medium"
        elif krabbypatty == "l":    
            total+=4
            krabbypatty = "Large"
    else:
        orderMasterList.append("No Sandwich")
    
    
    
    #order other meals
    orderInformation = "\nYour Order:\n"
    chooseSandwich,chooseFries,chooseDrink = False,False,False
    order = ["", "", "", 0]    
    order[other_index]=othermeal
    othermeal = input("Would you like to see our different meal list? (y,n)")
    if othermeal == "y":
        print(f'''
        Salty Sea Dog $1.25
        Footlong $2.00
        Sailors Suprise $3.00
        Golden Loaf $2.00 with sauce $2.50
    ''')
        othermeal = input("Would you like to buy from the meal list? (y,n)")
        if othermeal == "y":
            othermeal = input(f'''What would you like?
            Salty Sea Dog = ssd
            Footlong = ft
            Sailors Suprise = ss
            Golden Loaf = gl
            Golden Loaf with Cheese = glc
    ''')
            order[other_index]=othermeal
            if othermeal == "ssd":
                othermeal == "Salty Sea Dog"
                total+=1.25
            elif othermeal == "ft":
                othermeal == "Footlong"
                total+=2
            elif othermeal == "ss":
                othermeal == "Sailors Suprise"
                total+=3
            elif othermeal == "glc":
                othermeal == "Golden Loaf with Cheese"
                total+=2.5
        else:
            orderMasterList.append("No Other Meal")
                
                
                
    
    #Ordering Beverage
    drink = input(f'''Would you like a drink?
        Yes = y
        No = n
        ''')
    if drink == "y":
        chooseDrink=True
        drink = input(f'''What drink would you like?
        Seafoam Soda or Kelp Shake?
        Seafoam Soda = ss
        Kelp Shake = ks
    ''')
        if drink == "ss":
            orderMasterList.append("Seafoam Soda")
            orderInformation+=(f"\tDrink:\t\t{drink}\n")
            order[beverage_index]=drink   #replace whatever is in the order list
            drink == input(f'''What size would you like?
        Small = s
        Medium = m
        Large = l   
    ''')
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
            orderMasterList.append("Kelp Shake")
            orderInformation+=(f"\tDrink:\t\t{drink}\n")
            order[beverage_index]=drink   #replace whatever is in the order list
            
    else:
        orderMasterList.append("No Drink")
    
    
    
    #Coral Bits/Kelp Rings
    fries = input(f'''Would you like Coral Bits with that? Or Kelp Rings?
        Yes = y
        No = n
        Kelp Rings = ks
    ''')
    if fries == "y":
        chooseFries=True
        fries = input(f'''Which size? s,m,l 
        Small = s
        Medium = m
        Large = l
    ''')
        orderMasterList.append("Coral Bits")
        orderInformation+=(f"\tSide:\t\t{fries}\n")
        order[fries_index]=fries   #replace whatever is in the order list
        if fries == "s":
            fries="Small"
            total+=1
        elif fries == "m":
            fries="Medium"
            total+=1.75
        elif fries == "l":
            fries="Large"
            total+=2
    elif fries == "kr":
        fries = "Kelp Rings"
        total+=1.5
    else: 
        orderMasterList.append("No Side")



    #Salty Sauce
    saltysauce = int(input("How many salty sauce packets do you want? ($.25 ea) "))
    total+= (saltysauce*.5)
    orderInformation+=(f"\tSalty Sauce:\t{saltysauce}\n")
    order[salty_index]=saltysauce   #replace whatever is in the order list
    orderInformation+=(f"\tSubtotal: $\t{total}\n")
    
    
    
    #total with tax
    finaltotal = total
    finaltotal+=finaltotal*tax
    finaltotal = str(round(finaltotal, 2))
     #if in our list a "" exist
    if not("" in order):
        total-=1
        
        
    # print(orderInformation)

    orderPrintOut = (f'''
    Your order:
        Sandwich: {order[0]}
        Other Meal: {order[1]}
        Drink:        {order[2]}
        Side:         {order[3]}
        Salty Sauce:  {order[4]}
        Subtotal: ${total}
        Final Total: ${total}
    ​
    ''')

    orderMasterList.append(order)
    runningTotalPrintOut += orderPrintOut
    

    if (input("Do you want another order? (y/n)")=="n"):
        keepordering = False

      
print(orderMasterList)
print(runningTotalPrintOut)