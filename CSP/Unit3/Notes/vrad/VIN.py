class VIN:
    
    #constructor
    def __init__(self,v):
        #check if VIN valid
        if len(v) != 17:
            print(f"Invalid VIN: {v}")
            return v
        #Looping for invalid characters
        for c in v:
            if c in "IOQ":
                print(f"Invalid VIN: {v}")
                return v
           
        #wmi = first 3 characters
        self.wmi = v[0:3]
        #vds = second 6 with last being checksum
        self.vds = v[3:9]
        #ser = last 8 digits
        self.ser = v[9:]
    
        #toString
        def __str__(self):
            return self.wmi+self.vds+self.ser  
