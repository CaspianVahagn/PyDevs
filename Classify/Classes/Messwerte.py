'''
Created on 17.01.2018

@author: Dominik Reset
'''

class Messwerte:
    temperatur = 0
    zeit = ""
    
    def __init__(self,zeit,temperatur = None):
    
        
        if temperatur == None:
            if type(zeit) == tuple:
                self.zeit = zeit[0].replace('"',"")
                self.temperatur = zeit[1]
            else:
                
        
                zeit = zeit.split(",")
                self.zeit = zeit[0].replace('"',"")
                self.temperatur = float(zeit[1])
        else:
            self.zeit= zeit.replace('"',"")
            self.temperatur = float(temperatur)
            
    
    def __lt__(self,b):
        if self.zeit == b.zeit:
            return self.temperatur < b.temperatur
            
        return self.zeit < b.zeit
    
    def __gt__(self,b):
        if self.zeit == b.zeit:
            return self.temperatur > b.temperatur
            
        return self.zeit > b.zeit
    
    def __eq__(self,b):
        return (self.zeit == b.zeit and self.temperatur == b.temperatur)
    
    def __repr__(self):
        return 'Messwerte("'+self.zeit+'",'+ str(self.temperatur)+")"
    
    
    def get(self):
        return (self.zeit,self.temperatur)    
    
    def __getitem__(self, key):
        if key <= 0:
            return self.zeit
        else:
            return self.temperatur
        

        



