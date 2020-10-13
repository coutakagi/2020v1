'''
Created on 2019/12/30

@author: Takagi
'''

import numpy as np
import os


def getpathof(path0, sub):
    path=path0+"/"+sub+"/"
    checkpath(path)
    
    return path

def checkpath(path):
    if not os.path.exists(path):
        os.mkdir(path)
    path=os.path.abspath(path)
    return path

def savedatacsv(file, dt):    
    np.savetxt(file , dt,delimiter=",")

def savetextlist(fn,dt):
    with open(fn, 'wt') as f:
        for d in dt:
            f.writelines(d+"\n")
