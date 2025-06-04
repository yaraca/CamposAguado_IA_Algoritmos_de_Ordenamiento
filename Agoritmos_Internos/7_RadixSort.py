#RadixSort (Ordenamiento por radix o base)
#Algoritmo de ordenamiento no comparativo que ordena los números procesados dígito por dígito.
#Desde el dígito menos significativo al más significativo (LSB a MSB), o viceversa, dependiendo de la implementación.
#Utiliza un algoritmo de ordenamiento estable (como Counting Sort) como subrutina para ordenar los elementos según los dígitos.
#Funcionamiento:
# Encuentra el número con más dígitos (para saber cuántas pasadas se harán).
# Ordena la lista por el dígito menos significativo.
# Repite para cada posición del dígito (decenas, centenas, etc.).
# Al final, la lista queda ordenada.
#Aplicaciones: 
#ordenar números enteros grandes en tiempo casi lineal, sistemas financieros, bases de datos y aplicaciones que requieren ordenamiento rápido de números.

#Función para ordenar una lista utilizando Radix Sort
def counting_sort_por_digito(arr, exp):
    n = len(arr) #longitud del arreglo
    salida = [0] * n  #Arreglo de salida
    conteo = [0] * 10  #Contador para dígitos (0-9)

    #Contar ocurrencias de los dígitos
    for i in range(n): 
        indice = (arr[i] // exp) % 10 #obtener el dígito en la posición actual
        conteo[indice] += 1 #incrementar el contador para ese dígito

    #Convertir a posiciones reales
    for i in range(1, 10):
        conteo[i] += conteo[i - 1] #acumular los conteos para obtener las posiciones finales

    #Construir el arreglo de salida
    i = n - 1 #índice para recorrer el arreglo original desde el final
    while i >= 0: #mientras haya elementos por procesar
        indice = (arr[i] // exp) % 10 #obtener el dígito en la posición actual
        salida[conteo[indice] - 1] = arr[i] #colocar el elemento en la posición correcta en el arreglo de salida
        conteo[indice] -= 1 #decrementar el contador para ese dígito
        i -= 1

    #Copiar el arreglo ordenado al original
    for i in range(n):
        arr[i] = salida[i]

#Función principal de Radix Sort
def radix_sort(arr):
    # Encontrar el número máximo
    max_num = max(arr)
    exp = 1  #Representa la posición del dígito (1 = unidades, 10 = decenas, etc.)

    #Aplicar counting sort para cada dígito
    while max_num // exp > 0: 
        counting_sort_por_digito(arr, exp) #ordenar por el dígito actual
        exp *= 10 #incrementar la posición del dígito

# Ejemplo de uso
datos = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(datos)
print("Lista ordenada:", datos)

# Ejemplo de salida:
#Lista ordenada: [2, 24, 45, 66, 75, 90, 170, 802]
# como se puede ver, la lista se ordena de menor a mayor