
from numpy import inf

graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 1, 'G': 3}, 'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3, 'A': 1, 'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}

costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}


def search(source, target, graph, costs):
    '''
    Algoritmo de Dijkstra para encontrar las rutas más cortas
    ------
    Parameters
    source: str (indica el primer nodo)
    target: str (indica el nodo final)
    graph: dict
    cost: dict (función de costos asociada a cada nodo)

    -----
    Ejemplos
    costs = {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf, 'G': inf, 'H': inf, 'I': inf}
    graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 1, 'G': 3}, 'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3, 'A': 1, 'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}
    '''
    parents = {}
    nextNode = source
    
    #buscamos  mientras no hayamos llegaado al objetivo
    while nextNode != target:
        #hacemos la expansión de los  vecinos
        for neighbor in graph[nextNode]:
            #revisamos con el aloritmo de Dijkstra si la ruta es menor a la enterior
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                
                parents[neighbor] = nextNode
                
            del graph[neighbor][nextNode]
            
        del costs[nextNode]
        #vamos reduciendo a los valores mínimos de las rutas encontradas
        nextNode = min(costs, key=costs.get)
        #obtenemos el costo mínimo a partir del camino encontrado
    path=back(source,target,parents) #la función back revisa desde un punto dado hasta el nodo inicial la condicionalidad de ruta mínima
    
    return path,costs[target] 

result = search('A', 'B', graph, costs)




def back(source, target, searchResult):
    '''
    Función para ir eliminando los resultados del aloritmo de Dijkstraa
    -------
    Parameters
    source: str
    target: str
    searchResult: list (padres del nodo a buscar)
    '''
    node = target
    
    backpath = [target]
    
    path = []
    #revisamos hasta regresar al iniciio
    while node != source:
        
        backpath.append(searchResult[node])
        #buscamos  los valores de los padres del nodo ingresaado
        node = searchResult[node]
        
    for i in range(len(backpath)):
        #agregamos los valores de forma inversa
        path.append(backpath[-i - 1])
        
    return path




