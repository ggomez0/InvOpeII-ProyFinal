# Algoritmo de la ruta más corta (SPM) - Kruskal
import sys

print("")
print("-------- Algoritmo de la ruta más corta (SPM) - Kruskal--------")
print("")
class Graph:

	def __init__(self, vertices):
		self.V = vertices #Indica el nro de vertices
		self.graph = []
		# para almacenar el grafo

	# función para agregar un borde al gráfico
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# Una función de utilidad para encontrar el conjunto de un elemento 'i'
	
	def find(self, parent, i):
		if parent[i] != i:
		# Se reasigna el padre del nodo al nodo raíz como la compresión de ruta que se requiere
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	# Una función que hace la unión de dos conjuntos de x e y
    # Se utiliza la union por rango
	def union(self, parent, rank, x, y):
		
		# Se adjunta un árbol de clasificación más pequeño debajo de la raíz de 
        # árbol de alto rango (unión por rango)
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x

		# Si los rangos son los mismos, se asigna uno como raíz y se incrementa su rango en uno
		else:
			parent[y] = x
			rank[x] += 1

	# Esta es la función principal para construir MST usando Kruskal
		
	def KruskalMST(self):

		result = [] # Esto almacenará el MST resultante

		# Una variable de índice, utilizada para bordes ordenados
		i = 0

		# Una variable de índice, utilizada para result[]
		e = 0

		"""Todos los bordes en orden no decreciente de su peso. 
        Si no se nos permite cambiar el gráfico dado, podemos crear una copia del gráfico"""
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []

		# Crear subconjuntos V con elementos individuales
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# El número de aristas a tomar es igual a V-1
		while e < self.V - 1:

			# Se elije el borde más pequeño y se incrementa el índice para la próxima iteración
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# Si este borde no provoca un ciclo, entonces se incluye en el resultado y se incrementa el índice del resultado
            # para el borde siguiente
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# De lo contrario se descarta el borde

		minimumCost = 0
        
		print("Bordes en el MST construido")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree (MST) es: ", minimumCost)


if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# llamada de la funcion
	g.KruskalMST()

print("")
print("----------------------------------------------------- FIN ---------")
print("")
