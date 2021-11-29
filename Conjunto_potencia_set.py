conjunto_elementos = {
    'A',
    'B',
    'C',
    'D'
}

def Conjunto_Potencia_Set(conjunto_elementos):
    '''Función para calcular el conjunto potencia de una estructura de datos tipo conjunto
    
    
        Parámetros
            -----------------
            conjunto_elementos : set
        
        Ejemplo de conjunto:
            conjunto_elementos = {
                'A',
                'B',
                'C',
                'D'
            }
    '''    
    
    #Si se recibe como parámetro el conjunto vacío, se retorna el conjunto vacio
    if len(conjunto_elementos) == 0:
        return [set()]
    #En caso contrario, en primer lugar se realiza la copia del conjunto de entrada
    copia_conjunto = conjunto_elementos.copy()
    #Para cada elemento del conjunto se crea una copia del elemento en una variable
    for item in conjunto_elementos:
        it1 = item
    #Y posteriormente se elimina el primer elemento del conjunto del conjunto copia
    copia_conjunto.discard(it1)
    #Para volver a llamar recursivamente a la función con los elementos del conjunto restantes
    r = Conjunto_Potencia_Set(copia_conjunto)
    #Luego del último llamado se empieza a recorrer la lista retornda en cada llamado y se suma
    #cada uno de los elementos cuardados en la cariable de copia
    Lista = r + [s | {it1} for s in r] 
    return Lista    