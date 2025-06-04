#Selección (Selection Sort)
#Un algoritmos que divide la lista en dos partes: 
#Una parte ordenada al principio y otra parte no ordenada que se va reduciendo 
#Se selecciona el elemento más pequeño (o más grande) de la parte no ordenada y se pone al final de la parte ordenada en cada iteración.
#Funcionamiento: 
# Se recorre toda la lista para encontrar el mínimo.
# Se intercambia con el primer elemento.
# Luego se busca el siguiente mínimo y se intercambia con el segundo elemento.
# Así sucesivamente hasta que la lista esté ordenada.
#Es in place, lo que significa que no requiere memoria adicional para ordenar la lista.
#No es estable, ya que puede cambiar el orden de los elementos con el mismo valor.
#Aplicaciones:
#intercambios costosos, pero comparaciones baratas, entornos con restricciones de memoria, listas pequeñas o casi ordenadas.

def selection_sort(lista):
    n = len(lista)
    
    #recorrer todos los elementos de la lista
    for i in range(n):
        #suponer que el mínimo está en la posición actual
        indice_minimo = i

        #buscar el mínimo en el resto de la lista
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]: #comparar con el mínimo actual
                indice_minimo = j  #actualizar el índice del mínimo encontrado

        #intercambiar el elemento actual con el mínimo encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista

#Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
ordenados = selection_sort(numeros)
print("Lista ordenada:", ordenados)

#Ejemplo de salida:
#Lista ordenada: [11, 12, 22, 25, 64]
#como se puede ver, la lista se ordena de menor a mayor