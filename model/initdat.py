'''
Created on 2019/12/30

@author: Takagi
'''

import numpy as np


def getinitialdata(params):
    dt0=creataRandomMatrixnormal(params.n,params.n,params.initmat_sd)
    if params.inputtype==0:
        signal_input=createRandomInitial(params.n,params.rep, params.activation_probability)
    if params.inputtype==1:
        signal_input=createRandomInitialRange(params.n,params.bsize,params.brep, params.actpatterns,params.activation_max,params.activation_min)

    return [dt0, signal_input]

def creataRandomMatrixnormal(x,y,sd):
    pdat=np.random.normal(0.0,sd,x*y)
    pdat=np.array(pdat)
    pdat=np.reshape(pdat,(x,y))
    return pdat


def createRandomInitial(matrix_size, repeat_num, activation_probability):
    pdat=np.random.rand(repeat_num*matrix_size)
    pdat=np.array(pdat)
    pdat=np.reshape(pdat,(repeat_num,matrix_size))
    th1=1-activation_probability
    th2=activation_probability
    pdat=np.where((pdat<th1) &(pdat>th2),0,pdat)
    pdat=np.where((pdat>th1),1,pdat)
    pdat=np.where((pdat<th2) & (pdat>0),-1,pdat)
    return pdat

def createRandomInitialRange(matrix_size, bsize, brep, actpatterns, amax,amin):
    pdat=[]
    aprob=np.random.rand(actpatterns)
#    aprob=aprob/2.0
    adis=amax-amin
    aprob=adis*aprob+amin
    ssize=int(brep*bsize/actpatterns)
    for i in range(actpatterns):
        pdat0=thresholdactivity(matrix_size,ssize,aprob[i])
        pdat.extend(pdat0)
#        pdat.append(pdat0)
    pdat=np.array(pdat)
    repeat_num=bsize*brep
    pdat=np.reshape(pdat,(repeat_num,matrix_size))
    return pdat    
    
def thresholdactivity(matrix_size, repeat_num, activation_probability):
    pdat=np.random.rand(repeat_num*matrix_size)
    pdat=np.array(pdat)
    th1=1-activation_probability
    th2=activation_probability
    pdat=np.where((pdat<th1) &(pdat>th2),0,pdat)
    pdat=np.where((pdat>th1),1,pdat)
    pdat=np.where((pdat<th2) & (pdat>0),-1,pdat)
    return pdat

