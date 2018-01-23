'''
Created on 17.01.2018

@author: Dominik Reset
'''

from Classes.Messwerte import Messwerte
from Classes.Messreihe import Mengenreihe


from random import randint

def readfile():
    mw = []
    with open('messwerte.csv') as fp:
        for line in fp:
            mw.append(Messwerte(line)) 


            
    return mw
    
if __name__ == '__main__':
    mws = readfile()
    test = []
    for i in range(0,20):
        test.append(mws[randint(0,len(mws))])
        
    print("UNSORTED LIST:")
    for x in test: 
        print(x)
        
        
    print("SORTED LIST:")
    test = sorted(test)
    
    for x in test: 
       
        print(eval(repr(x))== x )
    
    
