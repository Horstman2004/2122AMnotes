total=0
sandwhich = input("What sandwhich woudl you like? Chicken ($5.25); Beef ($6.25); or Tofu ($5.75)? ")
if sandwhich == "c":
    total+=5.25
elif sandwhich == "b":
    total+=6.25
elif sandwhich == "t":
    total+=5.75

#iteration2
ui = input("Would you like a beverage: Yes or No?")
if ui == "n":
    print(f"Your sandwhich order: {sandwhich} {size} {total}")
elif ui == "y":
    size = input("What size? Small ($1.00); Medium ($1.75); Large ($2.25)")
    if size == "s":
        total+=1
    elif size == "m":
        total+=1.75
    elif size == "l":
        total+=2.25

print(f'''
Your sandwhich order: 
Sandwich: {sandwhich} 
Drink: {size} 
Subtotal: ${total}
''')