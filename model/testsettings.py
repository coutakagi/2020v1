'''
Created on 2019/12/30

@author: Takagi
'''

def setparams_single(smode,params):
   
    if smode==1:#test setting
        params.n=300
        params.totalset=3
        
#        params.bsize=10000#1000
        params.bsize=1000#1000
        params.brep=100#10
        params.actpatterns=100#10
        #4G input for bsize=10000 brep 100
        
        params.param_optimizer=0.001#0.01

        