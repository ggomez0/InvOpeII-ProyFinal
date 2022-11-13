# Algoritmo de la Ruta Critica (CPM)

import sys
from criticalpath import Node

# En este caso vamos a implementar el grafo en el mismo codigo
p = Node('project')
a = p.add(Node('A', duration=3))
b = p.add(Node('B', duration=3, lag=0))
c = p.add(Node('C', duration=4, lag=0))
d = p.add(Node('D', duration=6, lag=0))
e = p.add(Node('E', duration=5, lag=0))

# Tenemos un grafo armado de 5 nodos con sus repectivas relaciones y duraciones
print(p.link(a, b).link(a, c).link(a, d).link(b, e).link(c, e).link(d, e))

#Procesamos el grafo
p.update_all()

# y obtenemos la ruta critica con su duracion a traves de estos metodos
print("-------- Ruta Critica CPM --------")
print("")
print("* Esta es la ruta critica: ", p.get_critical_path())
print("y su duración es: ",p.duration)
print("")
print("----------------------------------------------------- FIN ---------")
print("")

