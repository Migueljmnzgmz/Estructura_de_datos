import numpy as np

#Creacion de una matriz 3x3
matriz_A= np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

for fila in matriz_A:
    for elemento in fila:
        print(elemento, end="")
    print("")

#  Acceder a un elemento (fila 1, columa 2)
elemento = matriz_A[1,2]
print(elemento)

#Modificar un elemento
matriz_A[0,0] = 99

