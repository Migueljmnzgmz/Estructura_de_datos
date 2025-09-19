# Ejercicio 4: Historial de Entrenamiento de un Modelo

def historial_entrenamiento():
    precisiones = []  # lista dinámica para almacenar valores
    print("=== Registro de precisión por época ===")
    print("Ingresa la precisión de cada época. Escribe 'fin' para terminar.\n")
    
    while True:
        entrada = input("Precisión de la época (0 a 100) o 'fin': ")
        if entrada.lower() == "fin":
            break
        try:
            valor = float(entrada)
            if 0 <= valor <= 100:
                precisiones.append(valor)
            else:
                print("⚠️ Ingresa un valor entre 0 y 100.")
        except ValueError:
            print("⚠️ Entrada no válida, intenta de nuevo.")
    
    # Resultados finales
    if len(precisiones) > 0:
        print("\n=== Resultados del Entrenamiento ===")
        print(f"Precisión final: {precisiones[-1]}%")
        print(f"Precisión más alta alcanzada: {max(precisiones)}%")
        print(f"Total de épocas registradas: {len(precisiones)}")
    else:
        print("No se ingresaron datos de precisión.")

# Ejecutar función
historial_entrenamiento()
# Ejercicio 4: Historial de Entrenamiento de un Modelo

def historial_entrenamiento():
    entrenamiento = []  # lista dinámica para almacenar valores
    print("=== Registro de precisión por época ===")
    print("Ingresa la precisión de cada época. Escribe 'fin' para terminar.\n")
    
    while True:
        entrada = input("Precisión de la época  o 'fin': ")
        if entrada.lower() == "fin":
            break
        try:
            valor = float(entrada)
            if 0 <= valor <= 1000000:
                entrenamiento.append(valor)
            else:
                print("Ingresa un valor entre 0 y 100.")
        except ValueError:
            print("Entrada no válida, intenta de nuevo.")
    
    # Resultados finales
    if len(entrenamiento) > 0:
        print("\n=== Resultados del Entrenamiento ===")
        print(f"Precisión final: {entrenamiento[-1]}%")
        print(f"Precisión más alta alcanzada: {max(entrenamiento)}%")

historial_entrenamiento()


