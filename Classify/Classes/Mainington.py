'''
Created on 17.01.2018

@author: Dominik Reset
'''

from Classes.Messwerte import Messwerte
from Classes.Messreihe import Mengenreihe


from random import randint

def readfile():
    mw = Mengenreihe();
    with open('messwerte.csv') as fp:
        for line in fp:
            mw.add(Messwerte(line)) 


            
    return mw
    
if __name__ == '__main__':
    mws = readfile()
    mws2 = Mengenreihe
    for i in range(0,20):
        mws2.add(str(mws[randint(0,len(mws))]))
        

    for x in mws[:5]:
        print(x)
        
    
    print(mws[:5].durchschnitt())
    print(mws["2013-07-15 16:30:01"])
    for s in mws2:
        print(s)
    
    mws2 = mws2.sorted()
    
    for s in mws2:
        print(s)
    
    print(mws2.min())
    print(mws2.max())
    
    