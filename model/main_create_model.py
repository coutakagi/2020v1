'''
Created on 2020/06/25

@author: Takagi
'''
import os

from utls import getpathof, checkpath  
from seq import exe_create_network
from paramset import ParamSetting
from testsettings import setparams_single
from savesetting import savesettingfile


mainpath0="./data/"
if not os.path.exists(mainpath0):
    os.mkdir(mainpath0)


mp=0.001#alpha for minimum activity
th=4.0#threshold for strength 
tr=3#total repeat
#mainpath=getpathof(mainpath0,"sd_"+str(th)) 
exepath=checkpath(mainpath0)
params=ParamSetting()
params.totalset=tr
params.energy_minlimit=mp
params.connecivity_limit=th
params.connecivity_limit_min=th
print("start")
                
#save setting and execute
savesettingfile(params,exepath)   
exe_create_network(exepath, params) 

print("end")