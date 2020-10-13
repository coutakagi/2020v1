'''
Created on 2019/12/30

@author: Takagi
'''
import numpy  as np

from netenenp import get_InOut_signal_Np, get_node_activity_cost_Np


def limit_networkmatrix(pdat, params):
    t0=params.connecivity_limit
    t1=params.connecivity_limit_min
    if t0>0:
        pdat=limitconnectivity(pdat, t0)
    if t1>0:
        pdat=limitconnectivity_min(pdat, t1)
        
    return pdat


def limitconnectivity_min(dt,t0):
    t=getWeightthreshold_inv(dt,t0)
    dt=np.where((dt>=0) & (dt<t),t,dt)
    dt=np.where((dt<0) & (dt>-t),-t,dt)
    return dt

def limitconnectivity(dt,t0):
    t=getWeightthreshold(dt,t0)
    dt=np.where(dt>t,t,dt)
    dt=np.where(dt<-t,-t,dt)
    return dt



def getWeightthreshold(pdat,mm):
    avsd= get_avr_sd(np.abs(pdat))
    thresh_val= avsd[0]+avsd[1]*mm
    return thresh_val


def getWeightthreshold_inv(pdat,mm):
    pinv=getinverseofdt(pdat)
    tv=getWeightthreshold(pinv,mm)
    ret=0
    if tv==0:
        ret=0
    else:
        ret=1.0/tv
    return ret

def get_avr_sd(pd):
    av= np.average(pd, None, None, False)
    sd=np.std(pd)
    ret= np.zeros(2)
    ret[0]=av
    ret[1]=sd
    return ret

def getinverseofdt(pdat0):
    pdat=np.copy(pdat0)
    pdat=np.where(pdat==0,1,pdat)
    pdat=1.0/pdat
    pc=np.copy(pdat0)
    pc=np.where(pc!=0,1,pc)
    ret=pdat*pc
    return ret

def getactivitycost(dt, sig0,params):
    oup0=get_InOut_signal_Np(dt,0.0,sig0)
    node_ene_sig=get_node_activity_cost_Np(np.abs(oup0), np.abs(oup0),np.abs(dt))   
    ret=np.mean(node_ene_sig)
    return ret

def normalizedt_atavr_ret(dt,aa):
    rt=aa
    dt=rt*dt
    return dt

def normalizedt_atavr(dt):
    aa=np.mean(np.abs(dt))
    if aa==0:
        aa=1
    rt=1/aa
    dt=rt*dt
    return dt, aa


def checkenergylimit(dt, sig, maa, params):
    aa=getactivitycost(dt, sig, params)
    if aa>0 :
        if maa>aa:
            rt=(maa)/(aa)
            dt=rt*dt
    return dt


def setsym_compare(dt, params):
    if params.symtype==0:
        return setsym_min(dt)
    if params.symtype==1:
        return setsym_max(dt)
    if params.symtype==2:
        return setsym_avr(dt)

def setsym(dt, params):
    return setsym_min(dt)

def setsym_min(dt):
    #select minimum
    st=np.abs(dt)-np.abs(dt.T)
    st=np.where(st<0,1,0)
    ret=st*dt+st.T*dt.T
    return ret

    
def setsym_max(dt):
    #select minimum
    st=np.abs(dt)-np.abs(dt.T)
    st=np.where(st>0,1,0)
    ret=st*dt+st.T*dt.T
    return ret


    
def setsym_avr(dt):
    #average
    ret=dt+dt.T
    ret=ret/2.0
    return ret