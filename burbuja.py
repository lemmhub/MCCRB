# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:33:29 2021

@author: Argenis Hernández García (MCC).
"""

def burbuja(a):
  '''Función para ordenar una lista de numeros de menor a mayo, 
    (forma ascendente).
    
      Parameters
          ----------
          a : list
      Ejemplo de ordenamiento:
          burbuja(a): [4, 5, 7, 2]
          Resultado: (-1, [(2, 3), (1, 2), (0, 1)], [2, 4, 5, 7])
'''
  #Recorrido de la lista (arreglo).
  t=[];k=len(a)
  while k>1:
      #Ordenamiento por rango
    for i in range(k-1):
      if a[i] > a[i+1] :
        t=t+[(i,i+1)]
        aux=a[i+1];a[i+1]=a[i]
        a[i]=aux
    k=k-1
  sgn=1
  #Condición residual
  if len(t)%2 :
    sgn=-1
    #Impresión de sgn, combinaciones y lista ordenada.
  return sgn,t,a