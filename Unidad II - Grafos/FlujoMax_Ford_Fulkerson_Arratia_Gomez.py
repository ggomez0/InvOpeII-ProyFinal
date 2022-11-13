# Algoritmo de Flujo Maximo - Método Ford Fulkerson

from collections import defaultdict
 
# En esta ocacion vamos a representar el grafo dirigido por medio de la matriz de adyacencia
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # grafo residual
        self. ROW = len(graph)
        # self.COL = len(gr[0])
 
    '''Se confirma, si existe una ruta desde la fuente 's' hasta el destino 't' en el 
    grafo'''
 
    def BFS(self, s, t, parent):
 
        # Se marcan todos los vértices como no visitados
        visited = [False]*(self.ROW)
 
        # Se crea una cola para BFS
        cola = []
 
        # Se marca el nodo de origen como visitado y se lo pone en la cola
        cola.append(s)
        visited[s] = True
 
         # while BFS
        while cola:
 
            # Para retirar un vértice de la cola e imprimirlo
            u = cola.pop(0)
 
            """Se obtiene todos los vértices adyacentes del vértice de 'u' eliminado de la cola.
                Si un adyacente no ha sido visitado, se marca como visitado y se lo pone en la cola"""
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                      # Si encontramos una conexión con el nodo sumidero, entonces BFS ya no tiene sentido.
                    # Solo tenemos que establecer su 'parent' y puede devolver como verdadero
                    cola.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 
        # Si no alcanzamos el sumidero en BFS a partir de la fuente, devolvera como falso
        return False
             
     
    # Devuelve el flujo máximo de s a t de acuerdo al grafo indicado
    def FordFulkerson(self, source, sink):
 
        # Este array esta lleno por BFS. De esta forma, podemos almacenar la ruta
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # Pra indicar que no hay flujo inicialmente
 
        # Se aumenta el flujo mientras haya un camino desde la fuente hasta el sumidero
        while self.BFS(source, sink, parent) :
 
            """Encuentre la capacidad residual mínima de los bordes a lo largo del camino llenado por BFS.
             O podemos hallar el flujo máximo a través del camino encontrado."""
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Se agrega el flujo de ruta al flujo general
            max_flow +=  path_flow
 
            # Se ctualizan las capacidades residuales de los bordes y los bordes inversos 
            # a lo largo de la ruta
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
  
# Aqui creamos el grafo
 
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
 
g = Graph(graph)
 
source = 0; sink = 5
print("") 
print("-------- Algoritmo de Flujo Maximo --------")
print("")  
print ("El flujo máximo posible es %d " % g.FordFulkerson(source, sink))
print("")
print("----------------------------------------------------- FIN ---------")
print("")