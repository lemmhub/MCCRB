"""
Programa para calcular el determinante de una Matriz {n} de forma recursiva.

"""



def delk(a,k): #A la funcion delk se le ingresan los parametros a y k
  '''
  Funcion para calcular el determinante menor de la Matriz A ----> A_{1,i}.
  -------
  Parameters
  a: List (determinante)
  k: int
  '''
  #El parametro n  se le asigna el tamaño de la matriz a, 
  n=len(a);b=zeros((n-1,n-1)) #
  
  #La iteracion i va de 1, hasta el tamaño n, para calcular el dterminante. 
  for i in range(1,n):
    # La iteracion j va hasta j para, completar el determinante a calcular de la matriz
    for j in range(n):
      
      if j<k:
        #Regresa el valor del determinante calculado
        b[i-1,j]=a[i,j]
      
      if j>k:
        #Regresa el valor del determinante calculado    
        b[i-1,j-1]=a[i,j]
  return b





#Ingresamos el valor de a.
def det(a): # a ---> es la matriz 
  '''
  Funcion para calcular el determinate de la Matriz A en forma recursiva
  a: arr (determinante)
  '''
  
  #n tomara el tamaño de valores que ingresamos en nuestra matriz a. 
  n=len(a) 

  # d es una variable bandera inicialidad en 0 para ser tomada en cuenta como contador.
  d=0
  
  #Aplicamos una condicion, si el tamaño de la matriz es 1 su determinante es 0
  if n==1:
    return a[0,0]
  
  for j in range(n): # for para iterar las columnas de 'j' en el tamaño de matriz
    
    #Valor de los Cofactores{ij}
    if j%2: #Aplicamos la operacion j%2
      s=-1.0 # Esto indica que tenemos un coeficiente negativo
   
    else:
      s=1.0 # de lo contrario es un coeficiente positivo
   
    d=d+s*a[0,j]*det(delk(a,j)) #Aplicamos la recursividad y llamamos a la funcion delk para calcular el determinante
  return d # regresa e valor del resultado del determinante







