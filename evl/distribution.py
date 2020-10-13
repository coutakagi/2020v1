'''
Created on 2020/10/02

@author: Takagi
'''
import numpy as np


def getdistribution_normalize(dts, dist_size):
    dg=getdistribution(dts, dist_size)
    dgnorm=normatmax(dg)
    return dgnorm

def getdistribution(dts, dist_size):
    dgs=[]
    for dt in dts:
        dg=np.sum(np.abs(dt),axis=1)
        dgs.append(dg)
    return getmultidistribution(dgs, dist_size)


def getdistribution_ax(dts, param):
    sn=param.dist_size
    dgs=[]
    for dt in dts:
        dg=np.sum(np.abs(dt),axis=0)
        dgs.append(dg)
    return getmultidistribution(dgs, sn)


def normatmax(dg):
    ma=np.max(dg)
    if ma==0:
        ma=1
    ret=np.copy(dg)
    ret=ret/ma
    return ret

def getmultidistribution(dgs, sn):
    dgs=np.array(dgs)
    dgs=dgs.reshape(-1)
    ret=setlinenum(dgs,sn)
    return ret


def setlinenum(dg0,sn):
    dg=dg0[dg0!=0]
    dg=np.sort(dg)[::-1]
    rl=len(dg)
    sflg=0
    if rl>sn:
        sflg=1
        return datasampling(dg,sn)

    if rl<sn:
        sflg=1
        return setsize_small(dg, sn)
    if sflg==0:
        return dg
        

def setlinenum_original(dg,sn):
    dg=np.sort(dg)[::-1]
    rl=len(dg)
    sflg=0
    if rl>sn:
        sflg=1
        return datasampling(dg,sn)

    if rl<sn:
        sflg=1
        return setsize_small(dg, sn)
    if sflg==0:
        return dg
        
def setsize_small(d, s):
    ret=np.zeros(s)
    s2=len(d)
    if s==0:
        s=1
    for i in range(s):
        ii=i/s
        ii=ii*s2
        ii=np.round(ii)
        ii=int(ii)
        if ii>=s2:
            ii=s2-1
        if ii<0:
            ii=0
        ret[i]=d[ii]
    return ret

def datasampling(dt, sn):
    dlen=len(dt)
    dd=dlen/(sn+1)
    stp=dd
    ret=np.zeros(sn)
    for i in range(sn):
        id=stp+dd*i
        ii=np.round(id)
        if ii<0:
            ii=0
        if ii>=dlen:
            ii=dlen-1
        ii=np.int(ii)
        ret[i]=dt[ii]
    return ret

def data_probability(sn):
    dd=1/(sn+1)
    stp=dd
    ret=[]
    for i in range(sn):
        id=stp+dd*i
        ret.append(id)
    return ret
  