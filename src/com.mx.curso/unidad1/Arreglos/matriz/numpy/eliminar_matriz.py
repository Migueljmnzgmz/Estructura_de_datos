import numpy as np

#Creacion de una matriz 3x4
#La segund colunma(indice 1) es la que se eliminara
datos= np.array([
    [10, 20, 30, 40],
    [15, 20, 35, 45],
    [25, 20, 45, 55]
])

print("Conjunto de datos original")
for fila in datos:
    for elemento in fila:
        print(elemento, end=" ")
    print()


#2 . Eliminar la columna de datos irrelevante
#np.delete() se utiliza para eliminar elementos o filas/columnas
# axis = 1 indica que se debe eliminar una columna
# El segundo argumento es el indice de la columna

datos_limpios = np.delete(datos, 2, axis=0)
print ("Conjunto de datos limpios ---")
print(datos_limpios)

#Valores para axis
#axis =1 -> columnas
#axis =0 -> Filas
#axis = none -> todo el array

datos_limpios2 =  np.delete (datos_limpios, 0, axis =1)

print("Conjunto de datos limpios procesados")
print(datos_limpios2)