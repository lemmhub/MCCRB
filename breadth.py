
graph = {
  'A' : ['B','C','Z'],
  'B' : ['D','E','A'],
  'C' : ['F','G','A'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : [],
  'Z':[]
}


def bfs(graph, node):
  '''Función para ordenar los grafos de acuerdo a un nodo solicitado
    
      Parameters
          ----------
          graph : dictionary
          node: Str    
      Ejemplo de grafo:
          graph = {
    'A' : ['B','C','Z'],
    'B' : ['D','E','A'],
    'C' : ['F','G','A'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
    'Z':[]
  }
  '''
  
  queue = []
  expand=[]
  visited = []
  visited.append(node)
  queue.append(node)
  # comenzamos la búsqueda en el nodo solicitado por el usuario
  while queue:
    #movemos los valores de queue a expand
    s = queue.pop(0) 
    expand.append(s)
    #Buscamos los vecinos indicados  en el  diccionario del grafo para  el nodo solicitado
    for neighbour in graph[s]:
      #Si  no se ha  llevado a visited  lo agregamos, y continuamos con los siguientes vecinos
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return expand
        
print(bfs(graph, 'B') )
      

