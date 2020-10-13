'''
Created on 2020/02/02

@author: Takagi
'''

import numpy as np

def get_InOut_signal_Np(mat, th, signal_input):
    output = get_output_signal_Np(mat, th, signal_input)
    oup=np.array(output)    
    return oup

def get_output_signal_Np(mat, th, signal_input):
    prod=np.dot(signal_input,mat)
    psig= set_ouput_signals_Np(prod, th)
    return psig



def get_node_activity_cost_Np(inp, oup, mat):
    cout=np.dot(inp.T, oup)
    cce=cout*mat
    pret=np.mean(cce, axis=0) 
    return pret

def set_ouput_signals_Np(pdat,sdv):
    th1=sdv
    th2=-sdv
    pdat=np.where((pdat<th1) &(pdat>th2),0,pdat)
    return pdat

