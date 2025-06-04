#Distribution of Initial Runs (distribución de secuencias iniciales)
#Su propósito es dividir un archivo de datos no ordenado en múltiples bloques (runs) que ya estén ordenados
#Para facilitar su posterior mezcla eficiente.
#Funcionamiento: 
# Lectura secuencial de los datos desde un archivo o lista.
# Se detectan segmentos crecientes que ya están ordenados (runs naturales).
# Cada uno de estos segmentos se almacena como una unidad separada.
# Estas secuencias se distribuyen entre archivos o listas auxiliares, para luego ser combinadas con algún algoritmo de mezcla.
#Aplicaciones:
# Ordenar grandes volúmenes de datos que no caben en memoria, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento externo eficiente.

#Función que encuentra secuencias crecientes (runs naturales) en una lista.
#Estas secuencias son útiles para ordenamientos externos como natural merging.
def distribuir_secuencias_iniciales(lista):
    runs = [] #lista para almacenar las secuencias (runs)
    run_actual = [] #lista para almacenar la secuencia actual

    for i in range(len(lista)): #recorrer la lista de datos
        if not run_actual or lista[i] >= run_actual[-1]: #si la secuencia actual está vacía o el elemento es mayor o igual al último de la secuencia
            run_actual.append(lista[i]) #agregar el elemento a la secuencia actual
        else: #si el elemento es menor que el último de la secuencia
            runs.append(run_actual) #agregar la secuencia actual a la lista de runs
            run_actual = [lista[i]] #iniciar una nueva secuencia con el elemento actual
    
    # Agrega el último run si existe
    if run_actual:
        runs.append(run_actual) 
    
    return runs

# Ejemplo de uso
datos = [3, 5, 7, 2, 4, 6, 1, 8]
runs = distribuir_secuencias_iniciales(datos)

# Imprimir resultados
print("Secuencias (runs) detectadas:")
for i, run in enumerate(runs): #para cada run encontrado
    print(f"Run {i+1}: {run}") #imprimir el run con su índice

#Ejemplo de salida:
# Secuencias (runs) detectadas:
# Run 1: [3, 5, 7]
# Run 2: [2, 4, 6]
# Run 3: [1, 8]
# Como se puede ver, las secuencias crecientes se han detectado correctamente.
# Esta función es útil para preparar datos para ordenamientos externos, como el natural merging.
