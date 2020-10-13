'''
Created on 2020/10/03

@author: Takagi
'''

import os

def getfilelist_all(mainpath0,subnames):
    ret=[]
    for sub in subnames:
        mainpath=os.path.join(mainpath0, sub)
        pret=getfilelist(mainpath)
        ret.append(pret)
    return ret


def getfilelist(mainpath):
    subname0="set"
    datfilename="result_matrix.csv"
    setnum=getsetunm(mainpath, subname0)   
    ret=[]
    for i in range(setnum):
        subname=subname0+str(i+1)
        fol=os.path.join(mainpath, subname)
        if os.path.exists(fol):
            fn=os.path.join(fol, datfilename)
            if os.path.exists(fn):
                ret.append(fn)
    return ret
            
        
    
        
def getsetunm(path, subname):
    fnl=os.listdir(path)
    e=0
    maxn=0
    for fn in fnl:
        fn=os.path.join(path, fn)
        if os.path.isdir(fn):
            fa=os.path.basename(fn)
            if len(fa)>len(subname):
                fe0=fa[len(subname):len(fa)]
    #            fe0=fa[0:(len(fa)-3)]
                if len(fe0)>0:
                    #print(fe0)
                    try:
                        n=int(fe0)
                        if n>maxn:
                            maxn=n
                    except:
                        e+=1
    return maxn
