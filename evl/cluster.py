'''
Created on 2020/10/02

@author: Takagi
'''

import numpy as np

def getclustersizes(dts, cluster_size):
    ret=[]
    ths=[]
    for dt in dts:
        pret, thv=getclustersizes_single(dt, cluster_size)
        ret.append(pret)
        ths.append(thv)
#    retm,_=getmaxmin(ret)
    reta,_=getavrandsds(ret)
    tha,_=getavrandsds(ths)
    reta=normatmax(reta)
    return reta, tha

def normatmax(reta):
    retm=np.max(np.abs(reta))
    if retm==0:
        retm=1
    reta=reta/retm
    return reta

def getmaxmin(pret):
    mav=np.max(np.abs(np.array(pret)),axis=0)
    miv=np.min(np.abs(np.array(pret)),axis=0)
    return mav, miv
def getavrandsds(pret):
    av=np.mean(np.array(pret),axis=0)
    sd=np.std(np.array(pret),axis=0)
    return av, sd

def getclustersizes_single(dt, cluster_size):
    ret=[]
    ths=getpercthreshold(cluster_size)#param.ths
    for th in ths:
        thv=getThresholdvalue(dt,th)
        res=getvalue(dt, thv)
        ret.append(res)
    return ret, ths


def getvalue(dt, thv):
    tdt=gettopolrep(dt,thv)
    cls=np.sum(tdt, axis=1)
    ret=np.max(cls)
    ns=dt.shape[1]
    if ns==0:
        ns=1
    ret=ret/ns
    return ret


def gettopolrep(dt,thv):
    ret=np.copy(dt)
    ret=np.where((ret>=-thv) & (ret<=thv),0,ret)
    ret=np.where(ret!=0,1,ret)
    return ret

def getpercthreshold(n0):
    n=n0+1
    #
    r=1.0/n0
    ret=[]
    for i in range(n):
        t=(i+1)*r
        t=round(t,3)
        ret.append(t)
    return ret




  
def getThresholdvalue(dt,prc):
    p=np.copy(np.abs(dt))
    p=np.array(p)
    p=p.reshape(-1)
    po=np.sort(p)[::-1]
    bb=len(p)*prc
    bb=np.round(bb)
    bb=int(bb)
    if bb<0:
        bb=0
    if bb>=len(p):
        bb=len(p)-1
    retv=po[bb]    
    return retv    



