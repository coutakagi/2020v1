'''
Created on 2019/12/30

@author: Takagi
'''
from utls import savedatacsv

def savedatainfold(setpath, step, dt0):
    
    savedatacsv(setpath+str(step)+".csv",dt0)
    
