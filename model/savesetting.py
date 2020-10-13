'''
Created on 2020/02/02

@author: Takagi
'''
from utls import savetextlist

def savesettingfile(param,folder):
    fname=folder+"/setting1.csv"
    savesettingfile_single(param,fname)

def savesettingfile_single(params,fname):
    nms=getsettingname()
    vls=getsettings(params)
    
    
    dtx=[]
    for i in range(len(nms)):
        d=nms[i]+","+str(vls[i])
        dtx.append(d)
    savetextlist(fname,dtx)
    
    

def getsettingname():
    ret=["n",
        "totalset",
        "bsize",
        "brep",
        "rep",
        "training_repeat",
        "param_optimizer",
        "energy_minlimit",
        "connecivity_limit",
        "connecivity_limit_min",
        "initmat_sd",
        "inputtype",
        "activation_probability",
        "activation_max",
        "activation_min",
        "actpatterns",        
        "ifdeb",
        "disp"]

    return ret

def getsettings(params):
    ret=[params.n,
        params.totalset,
        params.bsize,
        params.brep,
        params.rep,
        params.training_repeat,
        params.param_optimizer,
        params.energy_minlimit,
        params.connecivity_limit,
        params.connecivity_limit_min,
        params.initmat_sd,
        params.inputtype,
        params.activation_probability,
        params.activation_max,
        params.activation_min,
        params.actpatterns,
        params.ifdeb,
        params.disp]
    return ret

