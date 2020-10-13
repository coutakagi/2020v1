'''
Created on 2020/10/03

@author: Takagi
'''

import numpy as np

def getrmse(dts):
    pret=[]
    er=0
    for i in range(len(dts)):
        for j in range(len(dts)):
            if i>j:
                if dts[i].shape==dts[j].shape:
                    v=getdiff(dts[i],dts[j])
                    pret.append(v)
                else:
                    er+=1
    ret=np.mean(pret)
    return [ret]

def getrmse_value(dts):
    pret=[]
    er=0
    for i in range(len(dts)):
        for j in range(len(dts)):
            if i>j:
                if dts[i].shape==dts[j].shape:
                    v=getdiff(dts[i],dts[j])
                    pret.append(v)
                else:
                    er+=1
    ret=np.mean(pret)
    return ret

def getdiff(dt1, dt2):
    w1=getweight(dt1)
    w2=getweight(dt2)
    
    return getDiffValues(w1,w2) 


def getDiffValues(d1,d2):
    d1=np.sort(d1)
    d2=np.sort(d2)
    a1=np.mean(np.abs(d1))
    if a1==0:
        a1=1
    a2=np.mean(np.abs(d2))
    if a2==0:
        a2=1
    from sklearn.metrics import mean_squared_error
    n1=d1/a1
    n2=d2/a2
    m=mean_squared_error(n1,n2)
    m=np.sqrt(m)
    ret=[m]
    return ret


def getweight(dt):
    p=np.copy(dt)
    p=p.reshape(-1)
    p=np.abs(p)
    return p


