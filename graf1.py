graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
def generate_edges(graph):
  '''
  Función para generar las aristas de un grafo, de la forma
  graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

  --------
  Parameters
  graph: dict
  ---------
  return
  Lista de aristas indicando los nodos que conectan

  '''
  #creamos el arreglo receptor de aristas
  edges = []
  for node in graph:
    #revisamos  todos los vecinos en el nodo busucaado
    for neighbour in graph[node]:
      #agregamos la arista correspondiende en forma de una lista de aristas indicando los nodos que conectan
       edges.append((node, neighbour))
  return edges




def find_isolated_nodes(graph):
  '''
  Función para buscar nodos no conectados por aristas
  ------
  Parameters
  graph: dict
  '''

  isolated = []
  for node in graph:
    #comprobamos que no exista en el grafo enviado
    if not graph[node]:
      #ampliamos la lista 
      isolated=isolated+[node]
  return isolated

def vertex_degree(graph,vertex):
  '''
  Función para conocer el grado de un vértice
  ---------
  Parameters:
  graph: dict
  vertex: str
  '''

  #buscamos los vértices adyacentes al valor dado
  adj_vertices=graph[vertex]
  #generamos la cuenta del arreglo a partir de los propios vecinos del vértice y de los que son vecino a él que no hayan sido listados
  degree = len(adj_vertices) + adj_vertices.count(vertex)
  return degree


def graph_degree(graph):
  '''
  Función para encontrar el grado de un grafo
  ---------
  Parameters:
  graph: dict
  '''
  #comenzamos la cuenta en ceros
  degree_tot=0
  #buscamos cada elemento del gradfo
  for vertex in graph:
    #utilizamos la función vertex_degree para ir buscando el grado de cada vértice y añadirlo al total del grafo
    degree_tot=degree_tot+vertex_degree(graph,vertex)
  return degree_tot


def initq():
  return []


def enq(val):
  q.append(val)


def deq():
  u=q[0]
  q.remove(q[0])
  return u
# graph1 = {'A': ['B', 'C','E'],
#              'B': ['A','C', 'D'],
#              'C': ['D'],
#              'D': ['C'],
#              'E': ['F','D'],
#              'F': ['C']}
# graph = {'A': ['B', 'C'],
#              'B': ['A','C'],
#              'C': ['A',"B"]}
# graphw = {'A': [['B',2], ['C',4]],
#              'B': [['A',2],['C',1]],
#              'C': [['A',4],["B"]]}
# graphw1 = {'A': [['B',2], ['C',3],["D",2]],
#            'B': [['A',2],['D',1]],
#            'C': [['A',3],["D",4]],
#            "D": [["A",2],["B",1],["C",4]]
#           }



def BFS(graph,start,end):
  '''
  Función para realizar el recorrido de anchura de un grafo
  ----------
  Parameters
  graph: dict
  start: str
  end: str
  '''
  #iniciamos la búsqueda en el nodo de arranque
  temp_path = [start]	
  enq(temp_path)
  #buscamos que q no esté vacío
  while q != []:
    tmp_path = deq()
    last_node = tmp_path[len(tmp_path)-1]
    #imprimimos los valores temporales (nodos recorridos)
    print (tmp_path)
    if last_node == end:
      print ("VALID_PATH : ",tmp_path)
      #realizamos la búsqueda secuencial
    for link_node in graph[last_node]:
      if link_node not in tmp_path:
        new_path = []
        new_path = tmp_path + [link_node]
        enq(new_path)




def inits():
  return []

def push(val):
  s.append(val)

def pop():
  u=s[len(s)-1]
  s.remove(s[len(s)-1])
  return u

def DFS(graph,start,end):
  '''
  Función para realizar la búsqueda en profundidad dentro de un grafo
  ------
  Parameters:
  graph: dict
  start: str
  end: str
  '''
  # arrancamos la asignación del primer nodo, a partir de donde se busca 
  temp_path = [start]	
  push(temp_path)
  while s != []:
    tmp_path = pop()
    #buscamos el último nodo
    last_node = tmp_path[len(tmp_path)-1]
    print (tmp_path)
    #si en efecto es el último nodo entonces es una búsqueda correcta, de lo contrario falta ir más en profundidad
    if last_node == end:
      print ("VALID_PATH : ",tmp_path)
      #comienza la búsqueda en profundidad
    for link_node in graph[last_node]:
      if link_node not in tmp_path:
        new_path = [] 
        new_path = tmp_path + [link_node]
        push(new_path)



def add_vertex(graph,vertex):
  '''
  Función para agregar vértices en un grafo
  -------
  Parameters
  graph: dict
  vertex: str
  '''
  #buscamos que no exista el vértices 
  if vertex not in graph:
    #lo agregamos como un nuevo elemento del dict graph
    graph[vertex] = []
  return graph


def add_edge(graph,edge):
  '''
  Función para agregar 1 lado dentro de un grafo
  -------
  Parameters
  graph: dict
  edge: list (vertice1, vertice2)
  '''
  #parseamos la lista de lados a dos vértices
  (vertex1, vertex2) = tuple(edge)
  if vertex1 in graph:
    graph[vertex1].append(vertex2)
  else:
    graph[vertex1] = [vertex2]
  return graph


def generate_edges_weight(graph):
  '''
  Función para agregar pesos unitarios a un grafo
  -------
  Parameters
  graph: dict
  '''
  edges_weight = {}
  for node in graph:
    #busca los vecinos del diccionario
    for neighbour in graph[node]:
      #Comienza a agregar 1 acada ruta
       edges_weight[(node, neighbour[0])]=1
  return edges_weight



def min_edge(tree,fringe,edges_weight):
  '''
  Función para encontrar el número mínimo de lados en un árbol
  --------
  Parameters
  tree: dict
  fringe: dict
  edges_weight: dict
  '''
  min=10000
  for t in tree:
    for f in fringe:
      # buscamos los componentes del árbol como llaves de los pesos
      if (t,f) in edges_weight.keys():
        #si los valores son mínimos lo  traemos la función de entrega
        if edges_weight[(t,f)]<min:
          min=edges_weight[(t,f)];(tmin,fmin)=(t,f)
  return (tmin,fmin)






def dijkstra(graph,start,end):
  '''
  Algoritmo de Dijkstra para encontrar rutas más cortas
  -----------
  Parameters
  graph: dict
  start: str
  end: str
  '''

  #inicializamos diccionarios
  D={};P={}
  #buscamos los nodos como las llaves de los diccionarios
  for node in graph.keys():
    #Agregamos valores iniciales a los diccionarios
    D[node]=100
    P[node]=""
    #comenzamos en 0
  D[start]=0 
  #guardamos todas las llaves (nodos) del grafo
  unseen_nodes=graph.keys()
  #comenzamos la revisión de los grafos no visitados
  while len(unseen_nodes)>0:
    shortest=None
    node=""
    for temp_node in unseen_nodes:
      if shortest==None:
        shortest=D[temp_node]
        node=temp_node
        #revisamos que en efecto sean caminos más  cartos
      elif D[temp_node]<shortest:
        shortest=D[temp_node]
        node=temp_node
    unseen_nodes.remove(node)
    #Buscamos en todos los elementos (vecinos) de cada nodo del grafo
    for child_node,child_value in graph[node].items():
      #revisamos que los recorridos sean los m ás cortos
      if D[node]+child_value<D[child_node]:
        D[child_node]=D[node]+child_value
        P[child_node]=node 
  path=[]
  node=end
  #Si no es el nodo inicial
  while not(node==start):
    #continunamos la búsqueda de los demás elementos
    if path.count(node)==0:
      path.insert(0,node)
      node=P[node]
    else:
      break
  path.insert(0,start)
  return path
#  graphd={
#           "A":{"B":4,"C":3,"D":7},
#           "B":{"D":1,"F":4},
#           "C":{"D":3,"E":5},
#           "D":{"E":2,"F":2,"G":7},
#           "E":{"G":2},
#           "F":{"G":4},
#           "G":{},
#         }



def fleury(graph,start):
  '''
  Función para ejecutar el algoritmo  de Fleury para circuitos Eulerianos
  1. Empieza en un vértice si se tieneun circuito Euleriano
  2. Escoge cualquier lado dejando el vértice inicial, de tal forma que borrar el lado no separe el circuito
  3. Agrega el lado al circuito bórralo  del grrafo
  4. Continúa  hasta que  el circuito esté completo
  ------
  Parameters
  graph: dict
  start: str
  '''
  #Guardamos la variable de arranque
  nc=start
  #comenzamos las evaluaciones en 0
  lr=[];sr=[];sr.append(0);sp=0

  lr.append(start)
  #mientras el grafo no esté vacío
  while graph!={}:
    if graph[nc]==[]:
      #comenzamos la exploración  de lados
      del graph[nc]
      nc=sr[sp];sp=sp-1
      #agregamos los lados propuestos
      lr.append(nc)
    sr.append(0)
    sp=sp+1
    sr[sp]=nc
    nca=nc
    #buscamos que los lados estén en el grafo
    if graph[nc][0] not in graph:
      graph[nc].remove(graph[nc][0])
    nc=graph[nc][0]
    lr.append(nc)
    graph[nca].remove(nc)
    graph[nc].remove(nca)
    #revisaaamos que el  grafo en los nodos  adecuados no esté vacía
    if graph[nca]==[]:
      del graph[nca]
      sp=sp-1
  return lr



#graphe = {"a" : ["u","b"],
#"b" : ["a", "u"],
#"u" : ["a", "b", "d", "c"],
#"c" : ["d","u"],
#"d" : ["c","e","u","f"],
#"e" : ["f", "d"],
#"f" : ["e","d"]
#}