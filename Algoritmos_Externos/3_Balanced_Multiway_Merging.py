#Balanced Multiway Merging (Mezcla balanceada de múltiples vías)
#Es una técnica de ordenamiento externo que mejora la eficiencia del Straight y Natural Merging
#Utiliza más de dos archivos (vías) para leer y escribir simultáneamente durante la mezcla de datos.
#Funcionamiento:
# División de datos: Se dividen los datos en runs ordenados y se distribuyen equitativamente entre varios archivos de entrada.
# Lectura simultánea: Se leen varios runs a la vez (tantos como vías haya) y se combinan.
# Escritura en archivos de salida: Los resultados se escriben en archivos de salida, de forma balanceada.
# Intercambio de roles: En la siguiente pasada, los archivos de salida se convierten en archivos de entrada.
# Este proceso se repite hasta que todos los datos están ordenados en un único archivo.
#Aplicaciones:
#Ordenar grandes volúmenes de datos que no caben en memoria, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento externo eficiente.

#Simular 3 vías con listas en memoria

import heapq #para usar un heap en Python que permite una mezcla eficiente de múltiples vías
#heap es una estructura de datos que permite acceder al elemento más pequeño (o más grande) en tiempo constante y realizar inserciones y eliminaciones en tiempo logarítmico.

#Función para realizar una mezcla balanceada k-vías
#     1. Divide la lista en k sublistas ordenadas (runs).
#     2. Usa un heap para hacer mezcla eficiente.
def balanced_multiway_merge(lista, k):
    #Paso 1: Crear runs (sublistas ordenadas)
    longitud_run = len(lista) // k #longitud de cada run
    runs = [sorted(lista[i*longitud_run:(i+1)*longitud_run]) for i in range(k)] #crear k runs ordenados
    
    #Añadir el resto de elementos si la lista no se divide exactamente
    if len(lista) % k != 0: 
        runs[-1].extend(sorted(lista[k*longitud_run:]))
    
    #Paso 2: Mezclar con heap
    heap = [] # lista para el heap que contendrá los elementos de los runs
    indices = [0] * k  #índice actual en cada run
    
    resultado = [] #lista para almacenar el resultado final ordenado
    
    #Inicializar el heap con el primer elemento de cada run
    for i in range(k): #recorrer cada run
        if indices[i] < len(runs[i]): #si el run no está vacío
            heapq.heappush(heap, (runs[i][0], i)) #agregar el primer elemento del run al heap con su índice de origen
            # (valor, índice_run) 
    
    while heap: #mientras haya elementos en el heap
        valor, origen = heapq.heappop(heap) #obtener el elemento más pequeño del heap y su origen (run)
        resultado.append(valor) #agregar el valor al resultado final
        indices[origen] += 1 #avanzar el índice del run de origen
        if indices[origen] < len(runs[origen]): #si aún hay más elementos en el run de origen
            siguiente_valor = runs[origen][indices[origen]] #obtener el siguiente valor del run de origen
            heapq.heappush(heap, (siguiente_valor, origen)) #agregar el siguiente valor al heap con su índice de origen
    
    return resultado

# Ejemplo
datos = [18, 5, 9, 3, 22, 10, 7, 1, 15, 6]
ordenado = balanced_multiway_merge(datos, k=3) #k=3 vías
print("Lista ordenada:", ordenado)

# Ejemplo de salida:
# Lista ordenada: [1, 3, 5, 7, 9, 10, 15, 6, 18, 22]
# como se puede ver, la lista se ordena de menor a mayor