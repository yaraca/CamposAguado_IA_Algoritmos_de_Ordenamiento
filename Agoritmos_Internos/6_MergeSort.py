#Merge Sort (ordenamiento por mezcla)
#Es un algoritmos de ordenamiento basado en la técnica de divide y vencerás.
#La diferencia con QuickSort es que este sí es estable y tiene una complejidad de O(n log n) en todos los casos 
#O(n log n) es la complejidad temporal del algoritmo en el peor caso, caso promedio y mejor caso.
#Funcionamiento:
# Divide el arreglo en dos mitades.
# Aplica MergeSort recursivamente a cada mitad.
# Mezcla (merge) las dos mitades ordenadas para obtener el arreglo final.
#No es in place, ya que requiere memoria adicional para almacenar las mitades.
#Es estable, ya que no cambia el orden de los elementos con el mismo valor.
#Aplicaciones:
#util cuando se necesita un algoritmo estable, excelente para grandes conjuntos de datos, bases de datos y sistemas de archivos.

#MergeSort 
#Funcion para ordenar una lista utilizando el algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista  #Caso base: lista vacía o con un solo elemento

    medio = len(lista) // 2 #encontrar el punto medio de la lista
    izquierda = merge_sort(lista[:medio])    #Dividir la mitad izquierda
    derecha = merge_sort(lista[medio:])      #Dividirla mitad derecha

    return merge(izquierda, derecha)         #combinar ambas mitades ordenadas

#Función para mezclar dos listas ordenadas
def merge(izq, der):
    resultado = [] #lista para almacenar el resultado
    i = j = 0 #índices para recorrer las listas izquierda y derecha

    # Comparar y ordenar los elementos
    while i < len(izq) and j < len(der): #mientras haya elementos en ambas listas
        if izq[i] <= der[j]: #si el elemento de la izquierda es menor o igual al de la derecha
            resultado.append(izq[i]) #agregar el elemento de la izquierda al resultado
            i += 1 #avanzar el índice de la izquierda
        else: #si el elemento de la derecha es menor
            resultado.append(der[j]) #agregar el elemento de la derecha al resultado
            j += 1 #avanzar el índice de la derecha

    #Agregar los elementos restantes si los hay
    resultado.extend(izq[i:]) #agregar los elementos restantes de la izquierda
    resultado.extend(der[j:]) #agregar los elementos restantes de la derecha

    return resultado

# Ejemplo de uso
datos = [6, 3, 8, 5, 2, 7, 4, 1]
ordenados = merge_sort(datos)
print("Lista ordenada:", ordenados)

#Ejemplo de salida:
#Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8]
# como se puede ver, la lista se ordena de menor a mayor
