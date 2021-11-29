lista_elementos = [
    1,
    2,
    3,
    4
]

p = [
    1,
    2,
    3,
    4,
    5
]

m = 8

def selec(lista_elementos,p,m):
    '''Función que retorna los elementos de un conjunto potencia como valores de índice.
       estos índices son buscados en una lista p y suman los valores correpspondiente. Si la suma es menor al
       valor m, el elemento se incluye en una lista final.
      
        Parámetros
            -----------------
            lista_elementos  : list
            p : list
            m : Int
        
        Ejemplo de lista (debe ser de elementos únicamente numéricos):
            conjunto_elementos = [
                1,
                2,
                3,
                4
            ]
            
            p = [
                1,
                2,
                3,
                4,
                5
            ]
            
            La lista P debe tener un total de elementos de max(conjunto_elementos) + 1
        
    '''    
    #Se realiza el llamado a la función conjunto_potencia anterior
    s=conjunto_potencia(lista_elementos)
    r=[]
    #se realiza para cada uno de los elementos del conjunto potencia, el llamado a la función checa
    for i in s:
        if checa(i,p,m):
            #Si la función retorna true, añade los elementos del conjunto potencia que representan los índices
            #de la lista B que cuya suma es inferior al valor máximo m
            r=r+[i]
    return r


def checa(lst,p,m):
    '''Función auxiliar que verifica si la suma de los indices de cada uno de los elementos potencia
    en la lista B es mayor que el valor máximo recibido como parámetro
    '''
    s=0
    #Para cada elemento de cada uno de los sub conjuntos del conjunto potencia, usa el valor como indice
    #para extraer el dato en la lista b y sumarlos. Si la suma de todos los valores es menor al máximo
    #recibido, la función retorna true, en caso contrario, false.
    for k in lst:
        s=s+p[k]
    return s<m