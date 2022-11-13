import nashpy as nash;
import numpy as np;

A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
rps = nash.Game(A)
print("---------Nash-------------")
print(rps)
eqs = rps.support_enumeration()
print("")
print(list(eqs))
print("---------FIN-----------")



