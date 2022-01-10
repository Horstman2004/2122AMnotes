ui = input("Enter a word")

out = ""
for i in range(len(ui)):
    if i%2 == 0:
        out+=ui[i].upper()
    else:
        out+=ui[i]
    print(i)
print(out)