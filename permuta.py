# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:33:29 2021

@author: Argenis Hernández García (MCC).
"""

def inserta(x,lst,i):
  '''Función que inserta un valor x en la posición i de una lista.
    
      Parameters
          ----------
          x : valor
          lst: lista  
          i: posición
      Ejemplo de lista:
          lst = [1, 3, 5, 8, 9]
          inserta(4,lst,3):
              [1, 3, 5, 4, 8, 9]
  '''
    
  # Devuelve una lista resultado de insertar x en la posiciòn i
  return lst[:i]+[x]+lst[i:]

def inserta_multiple(x,lst):
  '''Función que inserta un valor x en todas las posiciones de una lista.
    
      Parameters
          ----------
          x : valor
          lst: lista  
      Ejemplo de lista:
          lst = [1, 3, 5, 4, 8, 9]
          inserta_multiple(2,lst):
 [[2, 1, 3, 5, 8, 9],
 [1, 2, 3, 5, 8, 9],
 [1, 3, 2, 5, 8, 9],
 [1, 3, 5, 2, 8, 9],
 [1, 3, 5, 8, 2, 9],
 [1, 3, 5, 8, 9, 2]]
'''
  # Devuelve una lista con el resultado de insertar x en todas las posiciones de lst.
  return [inserta(x,lst,i) for i in range(len(lst)+1)]

def permuta(c):
  '''Función que calcula y devuelve una lista de todas las permutaciones posibles 
  que se pueden hacer con los elemntos   contenidos en c.
    
      Parameters
          ----------
          c : lista contenida
      Ejemplo de permutaciones:
          c = [1, 3, 5]
          permuta(c):
              [[1, 3, 5], [3, 1, 5], [3, 5, 1], [1, 5, 3], [5, 1, 3], [5, 3, 1]]
  '''
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  return sum([inserta_multiple(c[0],i) for i in permuta(c[1:])],[])

def sgn(p):
  '''Función que Cuenta el número de inversiones en una permutaciòn p y calcula su  signo.
    
      Parameters
          ----------
          p : lista permutada
      Ejemplo de calculo:
          p = [[1, 3, 5], [3, 1, 5], [3, 5, 1], [1, 5, 3], [5, 1, 3], [5, 3, 1]]
          sgn(p):
              1
  '''
  # Cuenta el número de inversiones en una permutaciòn a y calcula su  signo
  count=0;i=-1;a=[]
  for k in range(len(p)):
    a=a+[p[k]]
  while i<len(a)-2:
    i=i+1
    if a[i]>a[i+1]:
      aux=a[i];a[i]=a[i+1];a[i+1]=aux
      count=count+1
      i=-1
      continue
  if count%2==0:
    return 1
  return -1

def det(a):
  '''Función que Calcula el determinante de la matriz a.
    
      Parameters
          ----------
          a: Matriz
      Ejemplo de calculo:
          det(a): ([[ 1, 0.],[ 0,0]])
          0
  '''
  # Calcula el determinante de la matris a 
  n=len(a)
  s=range(n)
  t=permuta1(s)
  d=0
  for u in t:
    r=sgn(u)
    for i in range(n):
      r=r*a[i,u[i]]
    d=d+r
  return d

def permuta1(c):
  '''Función que Calcula y devuelve una lista de todas las permutaciones 
  posibles que se pueden hacer con los elemntos   contenidos en c.
    
      Parameters
          ----------
          c: Lista
      Ejemplo de calculo:
          c = [1,3,5]
          permuta1(c):
              [[1, 3, 5], [3, 1, 5], [3, 5, 1], [1, 5, 3], [5, 1, 3], [5, 3, 1]]
  '''
  # Calcula y devuelve una lista de todas las permutaciones posibles que se pueden hacer con los 
  # elemntos   contenidos en c
  if len(c)==0:
    return [[]]
  lst=[]
  for i in permuta1(c[1:]):
    lst=lst+inserta_multiple(c[0],i)
  return lst