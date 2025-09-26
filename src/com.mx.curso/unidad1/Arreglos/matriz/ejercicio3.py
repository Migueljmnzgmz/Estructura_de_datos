import random
mapa = [[random.randint(0, 2) for _ in range(8)] for _ in range(8)]
print("Mapa de riesgo inicial:")
for fila in mapa:
    print(fila)
precaucion = 0
alto_riesgo = 0
for fila in mapa:
    precaucion += fila.count(1)
    alto_riesgo += fila.count(2)
print("Áreas de precaución:", precaucion)
print("Áreas de alto riesgo:", alto_riesgo)
for i in range(8):
    for j in range(8):
        if mapa[i][j] == 2:
            mapa[i][j] = 1
print("Mapa actualizado:")
for fila in mapa:
    print(fila)
