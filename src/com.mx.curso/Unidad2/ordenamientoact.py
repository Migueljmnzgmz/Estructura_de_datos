# Ordenamiento por selección aplicado a productos recomendados

productos = [
    {"nombre": "Laptop", "puntuacion": 82},
    {"nombre": "Audífonos", "puntuacion": 95},
    {"nombre": "Mouse", "puntuacion": 73},
    {"nombre": "Teclado", "puntuacion": 88},
    {"nombre": "Monitor", "puntuacion": 90}
]

print("Lista original:")
for p in productos:
    print(f"{p['nombre']}: {p['puntuacion']}")

# Ordena de menor a mayor puntuación
n = len(productos)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if productos[j]["puntuacion"] < productos[min_index]["puntuacion"]:
            min_index = j
    productos[i], productos[min_index] = productos[min_index], productos[i]

print("\nOrdenados de menor a mayor:")
for p in productos:
    print(f"{p['nombre']}: {p['puntuacion']}")

# Muestra de mayor a menor (más relevantes)
productos.reverse()

print("\nOrdenados de mayor a menor:")
for p in productos:
    print(f"{p['nombre']}: {p['puntuacion']}")
