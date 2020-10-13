'''
Created on 2020/06/25

@author: Takagi
'''
import os


def getlastset(path, sn, fintime):
    finfol=getlastfolder(path,sn, fintime)
    return finfol
    
def getlastfolder(path,sn, fintime):
    fnl=os.listdir(path)
    maxn=0
    for fn in fnl:
        fn=os.path.join(path, fn)
        if os.path.isdir(fn):
            n=getflodernum(fn, sn)
            if n>0:
                cflg=checkiffinal(fn,fintime)
                if n>maxn and cflg==1:
                    maxn=n
    return maxn

def checkiffinal(fold,fintime):
    ret=0
    fname=fold+"/training_1/"+str(fintime)+".csv"
    if os.path.exists(fname):
        ret=1
    return ret
    


def getflodernum(fn, sn):
    ret=0
    e=0
    fa=os.path.basename(fn)
    if len(fa)>len(sn):
        fe0=fa[len(sn):len(fa)]
        if len(fe0)>0:
            try:
                ret=int(fe0)
            except:
                e+=1
    return ret

