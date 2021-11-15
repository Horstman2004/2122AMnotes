#from file import class
from UnitConverter import UnitConverter

ui = f'''
    convert f to c = 1 
    convert c to f = 2
    convert c to k = 3
    convert f to k = 4
    convert k to c = 5
    convert k to f = 6
    quit = q
'''
u = input(ui)
while(u!="q"):
    if u==1:
        print(UnitConverter.fahrenheitToCelsius(int(input("Fah: "))
    elif u==2:
        print(UnitConverter.celsiusToFahrenheit(int(input("Cel: "))
    elif u==3:
        print(UnitConverter.celsiustokelvin(int(input("Cel: "))
    elif u==4:
        print(UnitConverter.fahrenheittokelvin(int(input("Fah: "))
    elif u==5:
        print(UnitConverter.kelvintocelsius(int(input("Kel: "))
    elif u==6:
        print(UnitConverter.kelvintofahrenheit(int(input("Kel: "))
