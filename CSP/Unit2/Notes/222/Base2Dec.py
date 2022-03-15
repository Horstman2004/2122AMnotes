letters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ui = input("Number Please ")
base = int(input("Base Please "))
highestExp = len(ui)-1
decimal=0
for n in ui:
    numba = letters.index(n)
    decimal+=(numba*base**highestExp)
    highestExp-+1
print(decimal)