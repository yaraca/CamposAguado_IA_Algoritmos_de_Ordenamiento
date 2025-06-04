#Intercambio (Bubble Sort)
#Algoritmo que compara pares adyacentes de elementos y los intercambia si están en el orden incorrecto 
#Repite este proceso hasta que no se necesiten más intercambios, lo que significa que la lista está ordenada.
#Funcionamiento:
# Compara el primer y segundo elemento.
# Si el primero es mayor, los intercambia.
# Repite hasta el final de la lista.
# Al final de cada pasada, el mayor valor "burbujea" al final.
# Repite el proceso ignorando el último elemento ya ordenado.
#Es in place, lo que significa que no requiere memoria adicional para ordenar la lista.
#Es estable, ya que no cambia el orden de los elementos con el mismo valor.
#Aplicaciones: 
#enseñanza y aprendizaje de algoritmos, listas pequeñas o casi ordenadas, entornos con restricciones de memoria.

def bubble_sort(lista):
    n = len(lista) #longitud de la lista

    #recorrer todos los elementos de la lista
    for i in range(n):
        #variable para detectar si hubo intercambio
        hubo_cambio = False

        #ultimos i elementos ya están en su lugar
        for j in range(0, n - i - 1): #se recorre hasta n-i-1 porque los últimos i elementos ya están ordenados
            if lista[j] > lista[j + 1]: #comparar el elemento actual con el siguiente adyacente
                #intercambiar si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j] 
                hubo_cambio = True #marcar que hubo un intercambio

        #si no hubo cambios, la lista ya está ordenada
        if not hubo_cambio:
            break

    return lista

# Ejemplo de uso
numeros = [5, 1, 4, 2, 8]
ordenados = bubble_sort(numeros)
print("Lista ordenada:", ordenados)

# Ejemplo de salida:
#Lista ordenada: [1, 2, 4, 5, 8]
# como se puede ver, la lista se ordena de menor a mayor