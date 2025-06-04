#Natural Merging (Mezcla Narural)
#Es una variante del método de mezcla externa (como el Straight Merging)
#Pero aprovecha los segmentos ya ordenados (runs naturales) que se encuentran en los datos de entrada para reducir el número de pasadas.
#Funcionamiento:
# Detección de runs naturales: Se recorren los datos buscando segmentos que ya están ordenados.
# Mezcla de runs: Se fusionan secuencialmente los runs encontrados, como en el método de mezcla directa.
# Repetición: El proceso se repite hasta que solo queda un run.
# Este método reduce el número de divisiones y pasadas, aprovechando el orden parcial de los datos.
#Aplicaciones:
#Ordenar grandes volúmenes de datos que contienen segmentos ordenados, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento externo eficiente.

#Función para encontrar runs naturales ya ordenados en una lista
def encontrar_runs_naturales(lista):
    runs = [] #lista para almacenar los runs encontrados
    run_actual = [lista[0]] #iniciar el primer run con el primer elemento de la lista
    
    for i in range(1, len(lista)): #recorrer la lista desde el segundo elemento
        if lista[i] >= lista[i - 1]: #si el elemento actual es mayor o igual al anterior
            run_actual.append(lista[i]) #agregar el elemento al run actual
        else: #si el elemento actual es menor que el anterior
            runs.append(run_actual) #agregar el run actual a la lista de runs
            run_actual = [lista[i]] #iniciar un nuevo run con el elemento actual
    
    runs.append(run_actual) #agregar el último run encontrado a la lista de runs
    return runs

#Función para fusionar dos runs ordenados
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

#Función principal para realizar el Natural Merging Sort
def natural_merge_sort(lista):
    runs = encontrar_runs_naturales(lista) #encontrar los runs naturales en la lista
    
    # Mezclar hasta que quede un solo run
    while len(runs) > 1:
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
datos = [3, 8, 12, 4, 5, 10, 2, 7]
ordenado = natural_merge_sort(datos)
print("Lista ordenada:", ordenado)

# Ejemplo de salida:
#Lista ordenada: [2, 3, 4, 5, 7, 8, 10, 12]
# como se puede ver, la lista se ordena de menor a mayor