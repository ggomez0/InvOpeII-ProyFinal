# Algoritmo MINIMAX

import nashpy as nash
import numpy as np

#Cargamos la matriz de juego en el codigo
A= np.array([[0,-1,1],[1,0,-1],[-1,1,0]])
# rps= nash.Game(A)
#rps
#El programa procede a encontrar los valores maxmin y minmax
maxmin = np.max(np.min(A,axis=1))
minmax = np.min(np.max(A,axis=0))
print("")
print("-------- Algoritmo MINI-MAX --------")
print("")
print("* Esta es la matriz de juego: ")
print(A)
print("")
print("valor maxmin: ",maxmin)
print ("valor minimax: ",minmax)
print("----------------------------------------------------- FIN ---------")
print("")



