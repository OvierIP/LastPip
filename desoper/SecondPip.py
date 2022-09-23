#!/usr/bin/env python3
r'''
SecondPip module
'''
#pip install anomalies
import numpy as np 
import pandas as pd
import random
import pandas as pd
from multiprocessing import Pool
import itertools
from anomalies import anomaly
import time
from itertools import permutations

def hello():
    r'''
    Hello function
    '''
    return 'Hello, World!'

def exponente(m):
    exp=(-1)**np.random.randint(0,2, size=m)   #la función exponente evita soluciones triviales o ceros 
    return exp

def exponente1(m):
    exp1=(-1)**np.random.randint(0,2, size=m+1)
    return exp1

def anomalyparimpar(n): #Este método halla una solución final Z para n par o impar; los ordena y los convierte en una tupla ascendente.
    if n % 2 == 0:    
    m=int(n/2-1)   
    l1 = np.random.randint(1, 19, size=m)*exponente(m) 
    k1 = np.random.randint(1, 19, size=m)*exponente(m) 
    l2 = l1[:m] 
    k2 = k1[:m]
    anomaly.free(l2,k2), anomaly.free.gcd, anomaly.free.simplified
    if 0 in anomaly.free.simplified: 
        return [None]
    if max(abs(anomaly.free.simplified))>32:
        return [None]
    if anomaly.free.simplified[0]<0:
        anomaly.free.simplified = -anomaly.free.simplified
    if ( 0 in [ sum(p) for p in itertools.permutations(anomaly.free.simplified, 2) ]): 
        return [None]
    else:
        return (np.sort(anomaly.free.simplified)).tolist()

  else:   
        m=int((n-3)/2)
        l1 = np.random.randint(1, 19, size=m)*exponente(m) 
        k1 = np.random.randint(1, 19, size=m+1)*exponente1(m) 
        l2 = l1[:m] 
        k2 = k1[:m+1]
        anomaly.free(l2,k2), anomaly.free.gcd, anomaly.free.simplified
        if 0 in anomaly.free.simplified:
          return [None]
        if anomaly.free.simplified[0]<0:
          anomaly.free.simplified = -anomaly.free.simplified
        if max(abs(anomaly.free.simplified))>32:
          return [None]
        if ( 0 in [ sum(p) for p in itertools.permutations(anomaly.free.simplified, 2) ]): 
          return [None]
        else:
          return (np.sort(anomaly.free.simplified)).tolist()
def all_sol_for_n(n):
  sol = [] 
  sol += [anomalyparimpar(n) for i in range(4000000)]
  final = [i for i in sol if i[0] is not None]
  return final

from multiprocessing import Pool
n = int(input("Por favor ingrese el valor de n que sea mayor que 4; "))
resultados = Pool().map(all_sol_for_n, list(range(n,n+1)))

df=pd.DataFrame(resultados)
df=df.T
df=df.astype(str)
df.drop_duplicates().reset_index(drop=True)


if __name__ == '__main__':  #En el main se guardan todas las funciones para que el programa consulte
    r'''
    Hello main
    '''
    hello()
    exponente(m)
    exponente1(m)
    anomalyparimpar(n)
    all_sol_for_n(n)
