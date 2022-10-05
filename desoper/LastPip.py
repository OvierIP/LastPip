import numpy as np 
import pandas as pd
import random
import pandas as pd
from multiprocessing import Pool
import itertools
from anomalies import anomaly
import time
from itertools import permutations

def exponente(m):
  
  '''
  la función exponente construye un arreglo de dimensión m
  '''
  
  exp=(-1)**np.random.randint(0,2, size=m)   
  return exp

def exponente1(m):
  
  '''
  la función exponente1 construye un arreglo de dimensión m
  '''
  
  exp1=(-1)**np.random.randint(0,2, size=m+1)
  return exp1

def anomalyparimpar(n): 
  
  ''' Esta función halla una solución final Z para un n par o impar;
  la ordena de menor a mayor y la convierte en un diccionario de listas 
  con claves l, k, z y gcd. Se verifica que no sea trivial, no se repita
  ni que supere un zmax.
  '''
  
  if n % 2 == 0:        

    m=int(n/2-1)   
    l1 = np.random.randint(1, 19, size=m)*exponente(m) 
    k1 = np.random.randint(1, 19, size=m)*exponente(m) 
    l2 = l1[:m] 
    k2 = k1[:m]
    anomaly.free(l2,k2), anomaly.free.gcd, anomaly.free.simplified
    if 0 in anomaly.free.simplified:         
      return {}
    if max(abs(anomaly.free.simplified))>30:
      return {}
    if anomaly.free.simplified[0]<0:
      anomaly.free.simplified = -anomaly.free.simplified
    if ( 0 in [ sum(p) for p in itertools.permutations(anomaly.free.simplified, 2) ]): 
      return {}
    else:
      return {"l":list(l2),"k":list(k2),"z":list(np.sort(anomaly.free.simplified)),"gcd":anomaly.free.gcd}

  else: 
    m=int((n-3)/2)
    l1 = np.random.randint(1, 19, size=m)*exponente(m) 
    k1 = np.random.randint(1, 19, size=m+1)*exponente1(m) 
    l2 = l1[:m] 
    k2 = k1[:m+1]
    anomaly.free(l2,k2), anomaly.free.gcd, anomaly.free.simplified
    if 0 in anomaly.free.simplified:
      return {}
    if anomaly.free.simplified[0]<0:
      anomaly.free.simplified = -anomaly.free.simplified
    if max(abs(anomaly.free.simplified))>30:
      return {}
    if ( 0 in [ sum(p) for p in itertools.permutations(anomaly.free.simplified, 2) ]): 
      return {}
    else:
      return {"l":list(l2),"k":list(k2),"z":list(np.sort(anomaly.free.simplified)),"gcd":anomaly.free.gcd}

def all_sol_for_n(n):
  
  ''' Esta función calcula el total de soluciones z para un n,
  y en un espacio de parámetros determinado. Los presenta en
  una lista de diccionarios
  '''
  
  sol = [] 
  sol += [anomalyparimpar(n) for i in range(500000)]
  sls=[d for d in sol if d]  
  return sls

def solutionfinal(n):
  ''' Esta función aplica multiprocessing para hallar las 
  soluciones finales, no repetidas y las presenta en un
  dataframe.
  '''
  
  from multiprocessing import Pool
  resultados = Pool().map(all_sol_for_n, list(range(n,n+1)))
  df=pd.DataFrame(resultados[0])
  df=df.astype(str)
  df=df.drop_duplicates(subset=['z']).reset_index(drop=True)
  return df
