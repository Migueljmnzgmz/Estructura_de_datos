# Ejercicio 2: Matriz de Conexiones para una Red Neuronal Simple
import time
# Matriz de pesos (3x2): 3 entradas -> 2 salidas
pesos = [
    [1, 2],   # Conexiones de la neurona 1 de entrada a las 2 de salida
    [2, 3],  # Conexiones de la neurona 2 de entrada
    [4, 5]    # Conexiones de la neurona 3 de entrada
]

entrada = [1, 2, 3]

# Calcular el producto punto: salida = entrada ⋅ pesos
salida = [0, 0]  # Inicializamos con 2 salidas en 0
star_time = time.time()
for j in range(2):  # para cada salida
    for i in range(3):  # para cada entrada
        salida[j] += entrada[i] * pesos[i][j]
end_time = time.time()

times = end_time - star_time

# Mostrar resultados
print("Vector de entrada:", entrada)
print("Matriz de pesos:")
for fila in pesos:
    print(fila)
print("Vector de salida:", salida)
print(times)
