sandwich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3
keepordering=True
orderMasterList=[]
runningTotalPrintOut=""
tax = .07

while(keepordering):

     total=0
     orderInformation = "\nYour Order:\n"
     chooseSandwich,chooseFries,chooseDrink = False,False,False
     order = ["", "", "", 0]     
     sandwhich = input("Would you like a sandwhich? (y.n)")
     if sandwhich == "y":
          sandwich = input("Which sandwich would you like:  chicken $5.25, beef $6.25, tofu $5.75 ")
          if sandwich=="c" or sandwich=="b" or sandwich=="t":
               orderInformation+=(f"\tSandwich:\t{sandwich}\n")
               order[sandwich_index]=sandwich   #replace whatever is in the order list
               chooseSandwich=True
          if sandwich == "c":
               total+=5.25
          elif sandwich == "b":
               total+=6.25
          elif sandwich == "t":    #needs to be an elif because if I spell it wrong, it will charge 5.75
               total+=5.75
     elif sandwhich == "n":
          orderMasterList.append("no sandwhich")

     #iteration 2
     drink = input("Would you like a drink? (y,n) ")
     if drink == "y":
          chooseDrink=True
          drink = input("Which size? s,m,l ")
          if drink == "s":
               total+=1
          elif drink == "m":
               total+=1.75
          elif drink == "l":
               #ask if they want a child size for $0.38 more
               drink = input("Would you like a child size for $.38 more? (y,n) ")
               if drink=="y":
                    total+=(2.25+.38)
                    drink="c"
               else:
                    total+=2.25
                    drink="l"
     elif drink == "n":
          orderMasterList.append("no drink")

          orderInformation+=(f"\tDrink:\t\t{drink}\n")
          order[beverage_index]=drink   #replace whatever is in the order list
          
     #iteration 3
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
          orderInformation+=(f"\tFries:\t\t{fries}\n")
          order[fries_index]=fries   #replace whatever is in the order list

     #iteration 4
     ketchup = int(input("How many ketchup packets do you want? ($.25 ea) "))
     total+= (ketchup*.25)
     orderInformation+=(f"\tKetchup:\t{ketchup}\n")
     order[ketchup_index]=ketchup   #replace whatever is in the order list

     # if chooseDrink and chooseFries and chooseSandwich:
     #      total-=1
     #total with tax
     finaltotal = total
     finaltotal+=finaltotal*tax
     finaltotal = str(round(finaltotal, 2))
     #if in our list a "" exist
     if not("" in order):
          total-=1
     #in checks to see if the item on left is in the item on right

     orderInformation+=(f"\tSubtotal: $\t{total}\n")
     # print(orderInformation)

     orderPrintOut = (f'''
     Your order:
          Sandwich:  {order[sandwich_index]}
          Drink:     {order[1]}
          Fries:     {order[2]}
          Ketchup:   {order[3]}
          Subtotal: ${total}
          Final Total: ${finaltotal}
     ​
     ''')

     orderMasterList.append(order)
     runningTotalPrintOut += orderPrintOut

     if (input("Do you want another order? (y/n)")=="n"):
          keepordering=False
print(orderMasterList)
print(runningTotalPrintOut)