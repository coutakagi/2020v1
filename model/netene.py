'''
Created on 2019/12/30

@author: Takagi
'''
import tensorflow as tf
import numpy as np




def networkEnergy(params, dt,sig):
    dimdt=[params.n,params.n, params.bsize] 
    oup0=get_InOut_signal(dt,0.0,sig,dimdt)
    node_ene=get_node_activity_cost(tf.abs(oup0), tf.abs(oup0),tf.abs(dt))
    w=getwirincost(dt)
    aw=divnorm(node_ene,w)
    ret=tf.reduce_mean(aw)
    return ret


def get_InOut_signal(mat, th, signal_input,dimdt):
    output = get_output_signal(mat, th, signal_input,dimdt)
    return output



def get_output_signal(mat, th, signal_input,dimdt):
    prod=tf.matmul(signal_input,mat)
    psig= set_ouput_signals(prod, th,dimdt)
    return psig


def set_ouput_signals(pdat,sdv,dimdt):
    th1=sdv
    th2=-sdv
    zr=createTFSubtMatrix(dimdt[2],dimdt[0],0)
    pdat=tf.where((pdat<th1) &(pdat>th2),zr,pdat)
    return pdat

def createTFSubtMatrix(x,y,v):
    zr=creataConstMatrix(x,y,v)
    zr=tf.constant(zr, dtype=tf.float64)
    return zr

def creataConstMatrix(x,y,v):
    pdat=np.full((x,y),v)
    pdat=np.array(pdat, dtype=np.float64)
    return pdat

def get_node_activity_cost(inp, oup, mat):
    cio=tf.matmul(tf.transpose(inp), oup)
    cce=cio*mat
    pret=tf.reduce_sum(cce,axis=0)
    return pret



def getwirincost(matth):
    w=tf.reduce_sum(tf.abs(matth),axis=0)

    return w

def divnorm(node_ene,w):
    z1=createconstantline(w.shape[0],1)
    w=tf.where(tf.equal(w,0), z1,w)
    ret=tf.divide(node_ene,w)
    return ret

def createconstantline(x,v):
    zr=creataConstline(x,v)
    zr=tf.constant(zr, dtype=tf.float64)
    return zr                

def creataConstline(x,v):
    pdat=np.full(x,v)
    pdat=np.array(pdat, dtype=np.float64)
    return pdat

