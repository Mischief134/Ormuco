class Compare:
    def __init__(self,value1:str,value2:str):
        super().__init__()
        self.value1 = value1
        self.value2 = value2

    def compare(self)->str:
        val_strip1=self.value1   #assign values of the class to a dummy variable since the string is modified
        val_strip2=self.value2

        #Strip the values of trailing ".0"
        while val_strip1.endswith("0") or val_strip2.endswith("0") or val_strip1.endswith(".") or val_strip2.endswith("."):
            val_strip1= self.rchop(val_strip1,"0")
            val_strip2= self.rchop(val_strip2,"0")
            val_strip1= self.rchop(val_strip1,".")
            val_strip2= self.rchop(val_strip2,".")

        #Split into array by getting rid of "." and convert values of array into int
        val1_split = list(map(int, val_strip1.split("."))) 
        val2_split = list(map(int, val_strip2.split("."))) 
        
        #Compare each value of array
        #Python does it automatically 

        if val1_split > val2_split:
            return self.value1 +" is greater than " +self.value2
        elif val1_split < val2_split:
            return self.value1 +" is smaller than " +self.value2
        else:
            return self.value1 +" is equal to " +self.value2
        
        

    def rchop(self,thestring, ending):       #chops off a substring from the end of the string
            if thestring.endswith(ending):
                return thestring[:-len(ending)]
            return thestring