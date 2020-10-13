

class ParamSetting(object):
    n=200#matrix size
    totalset=10#total test sets
    bsize=1000#batch size
    brep=10#repeat batch process
    rep=bsize*brep
    training_repeat=200#training epoch repeat
    param_optimizer=0.01#Adams optimizer parameter
    
    #limit settings
    energy_minlimit=0.001#activity cost minimum limit
    connecivity_limit=4.0#weight connectivity upper (SD)
    connecivity_limit_min=4.0#weight connectivity lower (SD)
    #initial setting 
    initmat_sd=0.5#matrix connection sd in normal distribution
    
    #input signal (training data setting)
    inputtype=1#0=fixed probability for activation, 1=random for each signal set
    activation_probability=0.2#for inputtype=0 
    activation_max=0.5
    activation_min=0.0
    actpatterns=10#number of different probability values
    
    symtype=0
    
    #debug or display results
    ifdeb=0
    disp=0
    
    def __init__(self):
        '''
        Constructor
        '''
         
