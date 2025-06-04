#Insercción (Insertion Sort)
#Algoritmo que construye una lista ordenada elemento por elemento
#Es similar a ordenar una mano de cartas
#Funcionamiento: 
#Se parte del segundo elemento de la lista y se compara con los elementos anteriores
#Si el elemento actual es menor que el anterior, se intercambian.
#Esto continúa hasta que el elemento actual esté en la posición correcta.
#Se repite el proceso para todos los elementos.
#Aplicaciones: 
#Listas pequeñas o casi ordenadas, comun en dispositivos con baja capacidad de memoria 

def insertion_sort(lista):
    #Recorrer desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        actual = lista[i]  #guardar el valor actual
        j = i - 1  #posición  anterior a la actual

        #mover elementos mayores al actual hacia la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]  #se desplaza el elemento
            j -= 1  #comparar hacia la izquierda

        #insertar el valor actual en su posición correcta
        lista[j + 1] = actual

    return lista

#Ejemplo de uso
datos = [5, 2, 4, 6, 1, 3]
ordenado = insertion_sort(datos)
print("Lista ordenada:", ordenado)

#Ejemplo de salida: 
#Lista ordenada: [1, 2, 3, 4, 5, 6]
#como se puede ver, la lista se ordena de menor a mayor
