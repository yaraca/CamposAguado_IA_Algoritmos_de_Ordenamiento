#QuickSort
#Es un algoritmo de ordenamiento eficiente que utiliza el enfoque de divide y vencerás.
#Funcionamiento: 
# Se selecciona un pivote (elemento de referencia).
# Se divide la lista en dos partes:
#   Elementos menores al pivote.
#   Elementos mayores o iguales al pivote.
# Se aplica recursivamente QuickSort a ambas sublistas.
# Se concatenan las sublistas ordenadas y el pivote.
#No es estable, ya que puede cambiar el orden de los elementos con el mismo valor.
#Es in place, ya que no requiere memoria adicional para ordenar la lista.
#Aplicaciones: 
#grandes conjuntos de datos en memoria, bases de datos, sistemas de archivos y aplicaciones que requieren ordenamiento rápido.

#QuickSort implementado de forma recursiva
def quicksort(lista):
    if len(lista) <= 1:
        return lista  # Caso base: lista vacía o de un solo elemento ya está ordenada
    else: #si la lista tiene más de un elemento
        pivote = lista[0]  #elegir el primer elemento como pivote
        menores = [x for x in lista[1:] if x < pivote]       #elementos menores al pivote
        mayores = [x for x in lista[1:] if x >= pivote]      #elementos mayores o iguales al pivote
        return quicksort(menores) + [pivote] + quicksort(mayores)  #aplicar recursión y combinar las sublistas ordenadas con el pivote

# Ejemplo de uso
datos = [8, 3, 1, 7, 0, 10, 2]
ordenados = quicksort(datos)
print("Lista ordenada:", ordenados)

# Ejemplo de salida:
#Lista ordenada: [0, 1, 2, 3, 7, 8, 10]
# como se puede ver, la lista se ordena de menor a mayor
