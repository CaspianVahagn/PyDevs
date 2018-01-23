'''
Created on 17.01.2018

@author: Dominik Reset
'''

from Classes.Messwerte import Messwerte 
import re
class Mengenreihe:
    
    _liste = []
   
     
    def __init__(self, mw = None):
        if(mw is not None):
            if type(mw) is list:
                self._liste = mw
            else:   
                self._liste.append(mw)
            
       
        self.n = len(self._liste);  
    
    def __len__(self):
        return len(self._liste)
    
    
    def add(self,werte):
        self._liste.append(werte)
        self.n = len(self)
        
     
        
    def __repr__(self):
        return "Mengenreihe(" + str(self._liste) + ")" 
    
    def __iter__(self):
        for x in self._liste:
            yield x
        
        
    def __getitem__(self, val):
        if type(val)is int:
            return self._liste[val]
        elif type(val) is slice:
            return Mengenreihe(self._liste[val])

        else:
           
            return Mengenreihe(list(filter(lambda x: x < Messwerte(val,0),self._liste)))
      
            
    
        
            
           
    
    def sorted(self):
        self._liste = self._liste.sorted()
        
        return self
       
    def min(self):
        return self.sorted()[0]
        
    def max(self):
        return self.sorted()[-1]
    
    
    def durchschnitt(self):
        moab = 0
        inti = 0
        for x in self._liste:
            moab += x[1]
            inti+=1
            
        print( str(moab) + ":" + str(len(self)))
        return moab/len(self)
        