import numpy as np

np.random.seed(42)
datos =np.random.randint(0, 100, (5, 5))

print("Base de datos original:\n", datos)

clean_data = np.delete(datos, 2, axis=1)
print ("Datos limpios:\n", clean_data)