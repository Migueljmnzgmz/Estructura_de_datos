#Analisis de complejidad de algoritmos
import time

def buscar_elemento(lista,elemento):
    for i in range(len(lista)):
        if lista[i]==elemento:
            return True
        return False

startime = time.time()
mi_lista = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,21,22,23,24,25,26,27,28,29,30]
elemento = 29
encontrado = buscar_elemento(mi_lista, elemento)
endtime= time.time()
if encontrado:
    print (f"El elemento {elemento} fue encontrado en la lista.")
else:
    print (f"El elemento {elemento} no fue encontrado en la lista")

print (f"Tiempo de ejecucion: {endtime - startime} segundos")