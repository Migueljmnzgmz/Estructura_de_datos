#Mapa riesgo

#Crear una matriz 8X8
matriz= [
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
    [0,1,2,1,2,0,1,1]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print (matriz[i][j], end="")
    print ()

area_riesgo=0 #2
area_precaucion=0 #1

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz [i][j]==2:
            area_riesgo +=1
        if matriz [i][j]==1:
            area_precaucion+=1
    print()

print(f"Area de riesgo (2): {area_riesgo}")
print(f"Area de precaucion (1): {area_precaucion}")


#Actalizar la matriz de navegacion
#Cambiar todos los 2 por 1

print("Actualizamos la matriz de navegacion")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==2:
            matriz[i][j]=1
    print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print (matriz[i][j], end="")
    print()
