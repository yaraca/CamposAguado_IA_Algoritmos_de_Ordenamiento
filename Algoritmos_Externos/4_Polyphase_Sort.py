#Polyphase Sort (Ordenamiento Polifásico)
#Es una mejora de la mezcla múltiple balanceada, que reduce la cantidad de archivos temporales necesarios 
#Al aprovechar una distribución asimétrica de los runs.
#Runs son segmentos de datos ordenados que se generan durante el proceso de ordenamiento.
#Funcionamiento:
# Distribución Inicial:
# Los datos se dividen en varios runs ordenados.
# Los runs no se distribuyen de forma pareja: se hace en una secuencia de Fibonacci.
# Ejemplo: si hay 3 archivos, los runs pueden distribuirse como: F(2)=1, F(3)=2, F(4)=3...
# Mezcla:
# Solo se usan dos archivos como entrada y uno como salida.
# En cada fase, los archivos cambian de rol para minimizar el uso de memoria y E/S.
# Fases:
# En cada fase se mezclan los runs y se escriben los nuevos runs en el archivo de salida.
# El proceso se repite hasta que todos los datos están ordenados en un solo archivo.
#Aplicaciones:
# Ordenar grandes volúmenes de datos que no caben en memoria, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento externo eficiente.

# Simula el ordenamiento polifásico con 3 archivos virtuales.
# Distribuye los runs en una secuencia similar a Fibonacci.

#Función para realizar el Polyphase Sort
def polyphase_sort(lista):
    from heapq import heappush, heappop #importar funciones para usar un heap en Python
    #heap es una estructura de datos que permite acceder al elemento más pequeño (o más grande) en tiempo constante y realizar inserciones y eliminaciones en tiempo logarítmico.
    #heappush: Inserta un elemento en el heap.
    #heappop: Elimina y devuelve el elemento más pequeño del heap.

    #Paso 1: Crear runs iniciales
    runs = [] #lista para almacenar los runs
    size = 2 #tamaño inicial del run, simula el incremento tipo Fibonacci
    i = 0 #índice para recorrer la lista original
    while i < len(lista): #mientras haya elementos en la lista original
        run = sorted(lista[i:i+size]) #obtener el run ordenado de tamaño 'size'
        runs.append(run) #agregar el run a la lista de runs
        i += size  #avanzar el índice de la lista original
        size += 1  #simula incremento tipo Fibonacci
    
    print("Runs iniciales distribuidos (estilo Fibonacci):")
    for idx, run in enumerate(runs): #enumerate para obtener el índice y el run
        print(f"Archivo {idx+1}: {run}") #imprimir los runs iniciales
    
    #Paso 2: Simulación de mezcla de runs con heap
    heap = [] #lista para el heap que contendrá los elementos de los runs
    indices = [0] * len(runs) #índices para rastrear la posición actual en cada run
    resultado = [] #lista para almacenar el resultado final ordenado

    while True: #mientras haya elementos para procesar
        activo = False #bandera para verificar si hay elementos activos en los runs
        for i in range(len(runs)): #recorrer cada run
            if indices[i] < len(runs[i]): #si el índice actual es menor que la longitud del run
                heappush(heap, (runs[i][indices[i]], i)) #agregar el elemento actual al heap con su índice de origen
                indices[i] += 1 #avanzar el índice del run
                activo = True #marcar que hay elementos activos
        
        if not activo: #si no hay elementos activos, salir del bucle
            break
        
        while heap: #mientras haya elementos en el heap
            val, origen = heappop(heap) #obtener el elemento más pequeño del heap y su origen (run)
            resultado.append(val) #agregar el valor al resultado final

    return resultado

# Ejemplo
datos = [12, 7, 25, 3, 18, 10, 1, 14]
ordenado = polyphase_sort(datos)
print("\nLista ordenada:", ordenado)

#Ejemplo de salida:
#Runs iniciales distribuidos (estilo Fibonacci):
# Archivo 1: [7, 12]
# Archivo 2: [3, 18, 25]
# Archivo 3: [1, 10, 14]

# Lista ordenada: [1, 3, 7, 10, 12, 18, 14, 25]
# como se puede ver, la lista se ordena de menor a mayor
#La salida muestra los runs iniciales distribuidos en archivos y el resultado final ordenado.
