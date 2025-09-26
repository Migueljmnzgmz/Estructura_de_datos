import numpy as np

datos = np.array([
    [10.9, 9.1, 20.1, 30.1],
    [5.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [7.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 20.1, 30.1],
    [10.9, 9.1, 10.1, 30.1]
])

print("Datos originales")
print(datos)

datos[5]=[99.99,99.99,99.99,99.99]

datos[0, 1] = np.nan
datos[5, 2] = np.nan
datos[9, 3] = np.nan

print("----- Datos con errores -----", datos)

datos_sin_errores= np.delete(datos,5,axis=0)
print("-----Datos sin errores----- ", datos_sin_errores)

media_columna= np.nanmean(datos_sin_errores, axis=0)
print("----- Media de cada columna -----", media_columna)


#Llenar los valores donde se encuentra nan por el promedio de cada columna
for i in range(datos.shape[0]):  # shape[0]= filas
    for j in range(datos.shape[1]): #shape[1]= columnas
        if np.isnan(datos[i,j]): #la funcion isnan evalua si es nan
            datos[i,j] = media_columna[j] #Toma la media columna y lo agrega a la posicion del nan

print("----- Datos sin errores y con nan reemplazados -----", datos)