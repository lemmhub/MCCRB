lista_elementos = [
    1,
    2,
    3,
    4
]

def conjunto_potencia(lista_elementos):
    '''Función para calcular el conjunto potencia de una lista
    
    
        Parámetros
            -----------------
            lista_elementos : list
        
        Ejemplo de lista:
            lista_elementos = [
            1,
            2,
            3,
            4
            ]
    '''    
    
    #Si la lista cuenta con un solo elemento, se retorna
    #la lista vacía más el elemento ingresado
    if len(lista_elementos)==1:
        return [[],lista_elementos]
    #En caso que hayan más de un elemento, se llama recursivamente
    #la función conjunto_potencia con los mismos elementos de la lista
    #inicial menos el primero
    lst=[]
    lista_b=conjunto_potencia(lista_elementos[1:])
    #Ya al finalizar los llamados recursivos, se utiliza un ciclo for
    #para leer los elementos extraidos en cada llamado y retornar los conjuntos elaborados
    for i in lista_b:
        aux=[lista_elementos[0]]+i
        lst=lst+[aux]
    return lista_b+lst