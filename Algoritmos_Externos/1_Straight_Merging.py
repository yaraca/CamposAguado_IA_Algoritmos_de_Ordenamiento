#Straight Merging (mezcla directa)
#Es un método de ordenamiento externo basado en el algoritmo MergeSort
#Diseñado para manejar archivos o conjuntos de datos que no caben en la memoria principal (RAM)
#Divide los datos en bloques o runs que caben en memoria, los ordena individualmente y luego los mezcla secuencialmente en archivos auxiliares
#Hasta obtener un único archivo ordenado.
#Funcionamiento: 
# División inicial: Se divide el archivo original en bloques pequeños (runs) que se pueden ordenar en memoria.
# Ordenamiento inicial: Cada bloque se ordena (por ejemplo, con Insertion Sort).
# Mezcla secuencial: Se realiza la mezcla (merge) de dos en dos bloques hasta que todo el archivo esté ordenado.
#Es secuencial y predecible, lo que la hace buena para medios como discos duros.
#Aplicaciones:
#Ordenar grandes volúmenes de datos que no caben en memoria, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento externo.

#ordenamiento externo en RAM, como si se tratara de archivos, usando listas
#Funcion para dividir una lista en bloques (runs) y ordenarlos individualmente
def dividir_en_runs(lista, tamaño_run):
    runs = [] #lista para almacenar los runs
    for i in range(0, len(lista), tamaño_run): #recorrer la lista en pasos del tamaño del run
        run = lista[i:i + tamaño_run] #obtener el bloque actual
        run.sort()  #Ordenamiento interno del bloque
        runs.append(run) #agregar el bloque ordenado a la lista de runs
    return runs

#Función para fusionar dos runs ordenados en uno solo
def mergear_dos_runs(run1, run2):
    resultado = [] #lista para almacenar el resultado de la mezcla
    i = j = 0 #índices para recorrer los runs
    while i < len(run1) and j < len(run2): #mientras haya elementos en ambos runs
        if run1[i] < run2[j]: #si el elemento del primer run es menor que el del segundo
            resultado.append(run1[i]) #agregar el elemento del primer run al resultado
            i += 1 #avanzar el índice del primer run
        else: #si el elemento del segundo run es menor o igual
            resultado.append(run2[j]) #agregar el elemento del segundo run al resultado
            j += 1 #avanzar el índice del segundo run
    resultado.extend(run1[i:]) #Agregar los elementos restantes del primer run si los hay
    resultado.extend(run2[j:]) #Agregar los elementos restantes del segundo run si los hay
    return resultado

#Función principal para realizar el Straight Merging Sort
def straight_merge_sort(lista, tamaño_run):
    """Simula mezcla directa para ordenar una lista grande."""
    runs = dividir_en_runs(lista, tamaño_run) #dividir la lista en runs y ordenarlos individualmente

    # Mezclar secuencialmente todos los runs
    while len(runs) > 1: #mientras haya más de un run
        nuevos_runs = [] #lista para almacenar los nuevos runs fusionados
        for i in range(0, len(runs), 2): #recorrer los runs de dos en dos
            if i + 1 < len(runs): #si hay un par de runs para fusionar
                merged = mergear_dos_runs(runs[i], runs[i + 1]) #fusionar los dos runs
                nuevos_runs.append(merged) #agregar el run fusionado a la lista de nuevos runs
            else: #si hay un run sin pareja (número impar de runs)
                nuevos_runs.append(runs[i]) #agregar el run sin pareja directamente a la lista de nuevos runs
        runs = nuevos_runs #actualizar la lista de runs con los nuevos runs fusionados
    return runs[0]

# Ejemplo de uso
datos = [12, 39, 5, 87, 4, 17, 55, 31, 21, 3]
ordenado = straight_merge_sort(datos, tamaño_run=4)
print("Lista ordenada:", ordenado)

# Ejemplo de salida:
#Lista ordenada: [3, 4, 5, 12, 17, 21, 31, 39, 55, 87]
# como se puede ver, la lista se ordena de menor a mayor