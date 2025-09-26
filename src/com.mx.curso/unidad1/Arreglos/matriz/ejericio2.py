pesos = [[0.2, 0.8], [0.6, 0.4], [0.5, 0.9]]
entrada = [1.0, 0.5, 0.2]
salida = [0, 0]
for j in range(2):
    for i in range(3):
        salida[j] += entrada[i] * pesos[i][j]
print("Entrada:", entrada)
print("Pesos:", pesos)
print("Salida:", salida)
