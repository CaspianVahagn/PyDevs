'''
Created on 17.01.2018

@author: Dominik Reset
'''

from Classes.Messwerte import Messwerte 
class Mengenreihe:
    
    _liste = []
     
    def __init__(self, mw = None):
        
        self._liste.append(mw)
     
    
    def __len__(self):
        return len(self._liste)
    
    
    def add(self,*werte):
        
        self._liste.append(werte)
        
     
        
        
    
    