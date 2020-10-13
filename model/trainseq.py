'''
Created on 2019/12/30

@author: Takagi
'''

import tensorflow as tf
import numpy as np

from netene import networkEnergy
from limitvariable import limit_networkmatrix, getactivitycost, normalizedt_atavr, normalizedt_atavr_ret, checkenergylimit
from limitvariable import setsym
from displayresult import savedatainfold



def train(setpaths, dts, params):
#    symstep=1000
    dt0=dts[0]
#    dt0=setsym_avr(dt0)
    signal_input=dts[1]
    setpath=setpaths[0]
    #set energy minimum limit by initial datasets
    actene_init=getactivitycost(dt0,signal_input,params)
    enelim=actene_init*params.energy_minlimit
    
    #define variables
    dt=tf.Variable(dt0)
    
    optimizer = tf.keras.optimizers.Adam(params.param_optimizer)
    optimizer_t = tf.keras.optimizers.Adam(params.param_optimizer)
    
    
    #start training
    bsize=params.bsize
    brep=params.brep
    for step in range(1+params.training_repeat):
        sff_idx = np.random.permutation(len(signal_input))
        rdt=dt.numpy()#np.array(dt)
        rdt=limit_networkmatrix(rdt, params)#set weight connection limit                 
        #training 
        rdt, aa=normalizedt_atavr(rdt)#set normalize before training
        dt=tf.Variable(rdt)
        for i in range(brep):
            idx_st=i*bsize
            idx_ed=(i+1)*bsize
            if idx_ed<=len(sff_idx):                    
                stin=signal_input[sff_idx[idx_st:idx_ed],:]
                #set energy and optimizer 
                with tf.GradientTape() as tape:
                    netene=networkEnergy(params,dt,tf.Variable(stin))
                grads = tape.gradient(netene, [dt])
                optimizer.apply_gradients(zip(grads,[dt])) 
                with tf.GradientTape() as tape_t:
                    netene_t=networkEnergy(params,tf.transpose(dt),tf.Variable(stin))
                grads_t = tape_t.gradient(netene_t, [dt])
                optimizer_t.apply_gradients(zip(grads_t,[dt]))

        rdt=dt.numpy()#dt#np.array(dt)
        rdt=normalizedt_atavr_ret(rdt,aa)#reset normalization
        #end training
        #check energy limit
        rdt=checkenergylimit(rdt,stin, enelim, params)
        #finalize 
        dt=tf.Variable(rdt)

#        if step==params.training_repeat or (step>0 and step%symstep==0):
        if step==params.training_repeat:
            ""
            #dt=tf.Variable(setsym(dt.numpy(), params))

        dt0=dt.numpy()
        #save data
        savedatainfold(setpath, step, dt0)
    return dt0







