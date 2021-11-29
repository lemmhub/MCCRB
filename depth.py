# Using a Python dictionary to act as an adjacency list
#!pip install networkx


graph2 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
graph1 = {
  'A' : ['B','C'],
  'B' : ['D','E'],
  'C' : ['F','G'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : []
}


graph = {
    'A' : ['B','C'],
    'B' : ['A', 'C'],
    'C' : ['A','B','D'],
    'D' : ['C','E','F','G'],
    'E' : ['F','G'],
    'F' : ['D','E'],
    'G' : ['D','E']
}

#generamos grafos de manera aleatoria, requiere la instalaciónde  networkx
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from([(3, 4), (5, 6)])
nx.draw_networkx(g, node_color='green', node_size=700)

visited = set() 
expand=[]

def dfs(graph, node):
    '''
    Función para recorrer en profundidad un grafo
    ------
    Parameters
    graph: dict
    node: str
    '''
    if node not in visited:
        expand.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)



def dfs_tree(graph, node_item):
    '''
    Función para recorrer en profundidad a un árbol
    ------
    Parameters
    graph: dict
    node_item: List str

    ejemplo:
    root=('A','A')
    dfs_tree(graph1, root)
    '''
    #Se extraen los valores de la lista de nodos
    (node,nodep)=node_item
    if node not in visited:
        print (node)
        #comienza a agregarse el total denodos
        visited.add(node)
        if node != nodep:
            #imprimimos los nodos recorridos
          print (node_item)
          #Agregamos las aristas del grafo
          edges_tree.append(node_item)
        for neighbour in graph[node]:
            #continuamos con los otros nodos
            node_item=(neighbour,node)
            dfs_tree(graph, node_item)
            
            

# Driver Code
dfs(graph1, 'A')
root=('A','A')
dfs_tree(graph1, root)