'''
Created on 2020/10/02

@author: Takagi
'''

import numpy as np

def load_matrixdata(filenames):
    ret=[]
    ret_flg=0
    for filename in filenames:
        dt,flg=readdata(filename)
        ret.append(dt)
        ret_flg+=flg
    return ret, ret_flg

def readdata(fn):
    import os
    flg=0
    #from utls import readDataCSV
    if os.path.exists(fn):
        ret=readDataCSV(fn)
    else:
        flg=1
        ret=None       
    return ret, flg


def readDataCSV(file):
    d= np.loadtxt(file,delimiter=",")
    return d




