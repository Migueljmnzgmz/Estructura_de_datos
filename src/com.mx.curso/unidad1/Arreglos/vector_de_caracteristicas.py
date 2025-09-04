import numpy as np

# Paso 1: Crear el vector de características con NumPy
vector = np.array([3.5, 1.4, 0.2])

print("Vector original:", vector)

# Paso 2: Calcular la suma total
suma_total = np.sum(vector)

# Paso 3: Normalizar el vector
vector_normalizado = vector / suma_total

print("Vector normalizado:", vector_normalizado)
print("Suma del vector normalizado:", np.sum(vector_normalizado))  # debería ser 1.0
