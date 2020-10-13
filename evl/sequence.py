'''
Created on 2020/10/02

@author: Takagi
'''

import numpy as np



def exe_stability_all(filenames_all,subnames,outputfilename_stability_all):
    from dataloadsave import load_matrixdata    
    from stability import getrmse_value
    ret=[]
    for filenames in filenames_all:
        dts, flg=load_matrixdata(filenames)
        if flg==0:
            rmse=getrmse_value(dts)
            ret.append(rmse)
        else:
            ret.append(-1.0)#error
    saveresult([subnames,ret],["Conditions","RMSE (w/<w>)"],outputfilename_stability_all)
    
        

def exe_stability(filenames,outputfilename_stability):
    from dataloadsave import load_matrixdata    
    dts, flg=load_matrixdata(filenames)
    from stability import getrmse
    if flg==0:
        rmse=getrmse(dts)
#        saveresult([ths,cs],["Threshold","max_cluster_size"],outputfilename_stability)
        saveresult([[rmse]],["RMSE (w/<w>)"],outputfilename_stability)
    else:
        print("load file error")    

def exe_clustersize(filenames,outputfilename_cluster, cluster_size):
    
    from dataloadsave import load_matrixdata    
    dts, flg=load_matrixdata(filenames)
    from cluster import getclustersizes
    if flg==0:
        cs, ths=getclustersizes(dts, cluster_size)
        saveresult([ths,cs],["Threshold","max_cluster_size"],outputfilename_cluster)
    else:
        print("load file error")

def exe_distribution(filenames,outputfilename, dist_size):
    
    from dataloadsave import load_matrixdata   
     
    dts, flg=load_matrixdata(filenames)
    from distribution import getdistribution_normalize, data_probability
    if flg==0:
        dg=getdistribution_normalize(dts, dist_size)
        dp=data_probability(dist_size)
        saveresult([dg,dp],["strength","cumulative_probability"],outputfilename)
    else:
        print("load file error")

def saveresult(dt, head, outputfilename):
    dt=np.array(dt).T
    tx=[]
    hh=""
    for h in head:
        hh+=h
        hh+=","
    tx.append(hh)
    
    for dd in dt:
        t=""
        for d in dd:
            t+=str(d)
            t+=","
        tx.append(t)
    savetextlist(outputfilename, tx)


def savetextlist(fn,dt):
    with open(fn, 'wt') as f:
        for d in dt:
            f.writelines(d+"\n")