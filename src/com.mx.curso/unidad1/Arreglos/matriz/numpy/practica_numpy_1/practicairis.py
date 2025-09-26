#practica con dataset iris
import numpy as np

#cargar el dataset
datos = np.genfromtxt('src/com.mx.curso/unidad1/Arreglos/matriz/numpy/practica_numpy_1/iris.data',
                        delimiter=',', dtype='object')
#visualizar los datos
print(datos)

#Cargar solo las primeras 4 columnas
datos_numericos = np.genfromtxt(
    'src/com.mx.curso/unidad1/Arreglos/matriz/numpy/practica_numpy_1/iris.data',
    delimiter=',',
    usecols=(0,1,2,3))

#Visuallizar los datos numericos
print(datos_numericos)

#Listado de indices a eliminar
indices_eliminar =[0,1,2,50]

#eliminar las filas con los indices detectados con error
datos_limpios = np.delete(datos_numericos, indices_eliminar, axis=0)

print ("----- Datos limpios -----", datos_limpios)

datos_limpios[0,0] = np.nan
datos_limpios[4,0] = np.nan
datos_limpios[12,1] = np.nan
datos_limpios[10,2] = np.nan
datos_limpios[10,0] = np.nan
datos_limpios[3,1] = np.nan
datos_limpios[10,2] = np.nan
datos_limpios[4,1] = np.nan
datos_limpios[5,0] = np.nan
datos_limpios[25,1] = np.nan

#Matriz con datos faltantes
print("----- Datos con Faltantes -----", datos_limpios)

media_columna= np.nanmean(datos_limpios, axis=0)
print("----- Media de cada columna -----", media_columna)

#Llenar los valores donde se encuentra nan por el promedio de cada columna
for i in range(datos_limpios.shape[0]):  # shape[0]= filas
    for j in range(datos_limpios.shape[1]): #shape[1]= columnas
        if np.isnan(datos_limpios[i,j]): #la funcion isnan evalua si es nan
            datos[i,j] = media_columna[j] #Toma la media columna y lo agrega a la posicion del nan4

print("----- Datos sin errores y con nan reemplazados -----", datos)