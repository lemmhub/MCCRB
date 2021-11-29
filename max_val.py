lista_de_indices = [
     [4],
     [3],
     [3, 4],
     [2],
     [2, 4],
     [2, 3],
     [2, 3, 4],
     [1],
     [1, 4],
     [1, 3],
     [1, 3, 4],
     [1, 2],
     [1, 2, 4],
     [1, 2, 3]
]

lista_de_valores = [
    1,
    2,
    3,
    4,
    5
]

def max_val(lista_de_indices,lista_de_valores):
    '''Función que retorna el valor máximo que suma los valores en una lista de datos, con una lista de
       índices a buscar en la lsita de datos y sumarlos.
      
        Parámetros
            -----------------
            lista_de_indices  : list of lists
            lista_de_valores  : list
        
        lista_de_indices = [
             [4],
             [3],
             [3, 4],
             [2],
             [2, 4],
             [2, 3],
             [2, 3, 4],
             [1],
             [1, 4],
             [1, 3],
             [1, 3, 4],
             [1, 2],
             [1, 2, 4],
             [1, 2, 3]
        ]

        lista_de_valores = [
            1,
            2,
            3,
            4,
            5
        ]
        Nota: La lista de valores debe contener un número de elementos mayor al máximo índice de la 
              lista_de_indices + 1.
    '''
    m_val=-1;m_sol=lista_de_indices[0]
    #El ciclo realiza la lectura de cada uno de los elementos en la lísta de índices
    for i in lista_de_indices:
        #Se invoca a la función auxiliar val para verificar si la suma de los valores en los indices de la
        #lista de valore es superior al máximo valor encontrado hasta ahora.
        if val(i,lista_de_valores)>m_val:
            m_val=val(i,lista_de_valores)
            m_sol=i
    #Se retorna el listado de índices y el valor de la suma de ellos en la lista de valores.
    return m_sol,m_val

def val(lst,b):
    '''Función auxiliar que recibe una lista de índices y una lista de datos. La función retorna
        la suma de los valores extraidos de los índices que se encuentran en la lista de índices 
    '''
    r=0
    for i in lst:
        r=r+b[i]
    return r