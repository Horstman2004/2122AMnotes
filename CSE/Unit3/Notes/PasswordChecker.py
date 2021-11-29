#         1#   1Cap. 1Low  1Speci 1Char
checklist = [False,False,False,False,False]
password = "abc123Ao!9"
specialcharacters = "!@#$%^&*()_+=[]}{\|~`-,./?<>"

#its harder to itterate
#check first, is it long enough
if len(password) >=8:
    checklist[4] = True

#loop through our password
for c in password:  #c stands for character
    #if there is a number
    if ord(c) in range(48,58):
        checklist[0] = True
    elif ord(c) in range(65,91):
        checklist[1] = True
    elif ord(c) in range(97,123):
        checklist[2] = True
    elif c in specialcharacters:
        checklist[3] = True
    

print(checklist)
if False in checklist:
    print("Your password describes you, weak.")
else:
    print("You have a strong password, but is it strong enough?...")