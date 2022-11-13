# Algoritmo para MST (Arbol de Mínima Expansión)

import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import tabulate

# Carga de la matriz de nodos y pesos

print("")
print(" ---------   Carga de la matriz del grafo --------")
print("")
f1=int(input('Ingrese la cantidad de nodos del grafo: '))
c1=f1
print("")

grafo = np.zeros((f1,c1))

print("")
print(" --------- Ingrese los elementos de la matriz ---------- ")
print("")

for f in range(0,f1):
    for c in range(0,c1):
        grafo[f,c] =  input("Ingrese el elemento A["+str(f+1)+";"+str(c+1)+"]: ")

print("---------------------------------------------------------------------")
print("")
print(" -- Este es el grafo cargado --")
print("")
mst_grafo = csr_matrix(grafo)
print(mst_grafo)
print("")
print("")
print("--------------------------------------------------------------------")
print(" ------- Este es el Arbol de Mínima Expansión (MST) del grafo ------")
print("--------------------------------------------------------------------")
print("")
Tcsr = minimum_spanning_tree(mst_grafo)
Tcsr.toarray().astype(int)
print(Tcsr)
print("")
print("----------------------------------------------------- FIN ---------")
print("")