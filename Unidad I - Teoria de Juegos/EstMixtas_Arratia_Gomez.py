from array import array
import numpy as np
import nashpy as nash

# Crear matriz de pago
A = np.array([[4, 0], [0, 2]])  # A es la fila del jugador
B = np.array([[2, 0], [0, 4]])  # B es la columna del jugador
game2 = nash.Game(A, B)
game2
# Encuentre el equilibrio de Nash
getEquilibrium= lambda: game2.support_enumeration()

print("-------Estrategias Mixtas---------")
print("3 lineas de salida")
eq = getEquilibrium()
for item in eq:
    print(item)

eq = getEquilibrium()
sigma_r, sigma_c = [array for array in eq][-1]
pd = nash.Game(A, B)

print()
print("Punto de equilibrio con estrategias mixtas")
print(pd[sigma_r, sigma_c])
print("-------------FIN-------------------")
