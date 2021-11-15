class UnitConverter:
    
    #c to f
    #static method, you don't need self
    @staticmethod   #@ symbol is a decorator
    def celsiusToFahrenheit(c):
        fah = c*9/5+32
        return fah
    
    #f to c
    def fahrenheitToCelsius(f):
        cel = (f-32)*5/9
        return cel
    
    #c to k
    @staticmethod
    def celsiustokelvin(c):
        k = c+273.15
        return k
    
    #f to k
    @staticmethod
    def fahrenheittokelvin(f):
        k = f*5/9+273.15
        return k

    #k to c
    @staticmethod
    def kelvintocelsius(k):
        cel = k-273.15
        return k

    #k to f
    @staticmethod
    def kelvintofahrenheit(k):
        fah = k*9/5+32
        return k