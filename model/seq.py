'''
Created on 2019/12/30

@author: Takagi
'''

from initdat import getinitialdata
from utls import savedatacsv
from trainseq import train 
from utls import getpathof
from pathcheck_training import getlastset

def exe_create_network(mainpath, params):
    s0=0
    if params.ifdeb==0:
        s0=getlastset(mainpath, "set", params.training_repeat)
        
    if params.totalset-s0>0:
        if s0!=0:
            print("restart from {} ".format(s0+1))
        else:
            ""        
        for s1 in range(params.totalset-s0):
            s=s0+s1
            print("set: {} / {}".format(s+1,params.totalset))
            setpath=getpathof(mainpath,"set"+str(s+1))
            dt=networktraining(setpath,params)
            savedatacsv(setpath+"result_matrix.csv",dt)
    else:
        print("skip already exists")



def networktraining(setpath,params):
    
    dts=getinitialdata(params)
    savedatacsv(setpath+"initial_matrix.csv",dts[0])
    savedatacsv(setpath+"initial_inputsignal.csv",dts[1])
    
    setpath_pre=getpathof(setpath,"training_1")
    dt=train([setpath_pre], dts, params)
    dts[0]=dt
    return dt


