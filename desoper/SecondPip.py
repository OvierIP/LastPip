#!/usr/bin/env python3
import dask.array as da
import pandas as pd
from multiprocessing import Pool
from multiprocessing import cpu_count
import os
import numpy as np
import itertools
import sys
from anomalies import anomaly
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")
global zmax
zmax=32

z=anomaly.free

def _get_chiral(q,q_max=np.inf):
    #Normalize to positive minimum
    if 0 in q:
        #q=q[q!=0]
        return None,None
    if q.size==0:
        return None,None
    if q[0]<0:
        q=-q
    #Divide by GCD
    GCD=np.gcd.reduce(q)
    q=(q/GCD).astype(int)
    if ( #not 0 in z and 
          0 not in [ sum(p) for p in itertools.permutations(q, 2) ] and #avoid vector-like and multiple 0's
          np.abs(q).max()<=q_max
           ):
        return q,GCD
    else:
        return None,None
    
def get_solution(l,k,zmax=zmax):
    q,gcd=_get_chiral( z(l,k) )
    #if q is not None and np.abs(q).max()<=zmax:#
    if q is not None and np.abs(q).max()<=zmax:
        return {'l':l,'k':k,'z':list(q),'gcd':gcd}
    else:
        return {}    
    
def get_solution_from_list(lk,zmax=zmax):
    n=len(lk)
    l=lk[:n//2]
    k=lk[n//2:]
    return get_solution(l,k,zmax)

def principal(n,m,imax,zmax,N):

    df=pd.DataFrame()

    long =(2*m+1)**(n-2)
    size_old =0
    i=0 
    d_size=1
    while d_size>0:
        ll=da.random.randint(-m,m+1,(N,n-2))
        ll=ll.to_dask_dataframe().drop_duplicates().to_dask_array()
        ll=ll.compute()
        s=time.time()
        pool = Pool(cpu_count())

        sls = pool.map(get_solution_from_list,ll)
         
        pool.close()
        del ll

        sls=[d for d in sls if d]
        df=df.append(  sls,ignore_index=True    )

        df.sort_values('gcd')
        df['zs']=df['z'].astype(str)
        df=df.drop_duplicates('zs').drop('zs',axis='columns').reset_index(drop=True)
        d_size=df.shape[0]-size_old
        if d_size>0:
            size_old=df.shape[0]
        if i>=imax:
            break
    return df    
