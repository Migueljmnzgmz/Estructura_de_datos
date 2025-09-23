#Operaciones de limpieza de datos
import numpy as np
datos = np.array([[10,10,10],
                  [20,20,20],
                  [30,30,30]])

print ("Datos originales", datos)

datos_limpios = np.delete(datos, 1, axis=0) #Elimina la segunda fila
print("Datos limpios de eliminar la segunda fila: \n", datos_limpios)

#Introducir datos erroneos
datos[0] = [-1, -2, -2]
datos[1] = [20, -2, 20]
datos[2] = [30, 30, 30]
print("Bases de datos con errores introducidos: \n", datos)

valor_negativos =[]
for i in range(datos.shape[0]):
    for j in range(datos.shape[1]):
        if datos[i,j]<0:
            valor_negativos.append([i,j])


datos_limpios = np.delete(datos, valor_negativos, axis=0) #Eliminar datos negativos
print("Datos limpios despues de eliminar numeros negativos", datos_limpios)