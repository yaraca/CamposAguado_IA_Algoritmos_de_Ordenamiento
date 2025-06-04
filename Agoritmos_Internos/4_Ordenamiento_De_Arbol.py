#Ordenamiento de Arbol (Tree Sort)
#Un algoritmo de ordenamiento basado en una estructura de arbol binario de búsqueda (BST)
#Inserta los elementos en un BST y luego los recupera en orden en el recorrido inordenado (in-order)
#Funcionamiento:
# Se construye un árbol binario de búsqueda con los elementos.
# Luego se recorre el árbol en inorden, obteniendo una lista ordenada.
#No es in place, ya que requiere memoria adicional para el árbol.
#Es estable, ya que no cambia el orden de los elementos con el mismo valor.
#Aplicaciones:
#util para maneter una colección ordenada dinámicamente, conjuntos grandes de datos, bases de datos y sistemas de archivos.

#Clase para nodo de un árbol binario de búsqueda
class NodoArbol:
    #Función constructora para inicializar el nodo
    def __init__(self, valor): 
        self.valor = valor #valor del nodo
        self.izquierdo = None #hijo izquierdo del nodo
        self.derecho = None #hijo derecho del nodo

#Función para insertar un valor en el BST
def insertar(nodo, valor):
    if nodo is None: #si el nodo es None, significa que es un lugar vacío para insertar
        return NodoArbol(valor) #retorna un nuevo nodo con el valor
    if valor < nodo.valor: #si el valor es menor que el del nodo actual, se inserta en el subárbol izquierdo
        nodo.izquierdo = insertar(nodo.izquierdo, valor) 
    else: #si el valor es mayor o igual, se inserta en el subárbol derecho
        nodo.derecho = insertar(nodo.derecho, valor)
    return nodo

#Función para recorrer el árbol en inorden y agregar elementos ordenados
def recorrido_inorden(nodo, resultado):
    if nodo: #si el nodo no es None, se recorre
        recorrido_inorden(nodo.izquierdo, resultado) #recorrer el subárbol izquierdo
        resultado.append(nodo.valor) #agregar el valor del nodo actual a la lista de resultados
        recorrido_inorden(nodo.derecho, resultado) #recorrer el subárbol derecho

#Función principal de Tree Sort
def tree_sort(lista):
    raiz = None #inicializar la raíz del árbol como None
    for valor in lista: #recorrer cada valor en la lista
        raiz = insertar(raiz, valor) #insertar el valor en el árbol
    
    resultado = [] #lista para almacenar los valores ordenados
    recorrido_inorden(raiz, resultado) #recorrer el árbol en inorden y llenar la lista de resultados
    return resultado #retornar la lista ordenada

# Ejemplo de uso
datos = [5, 3, 7, 2, 8, 1]
ordenados = tree_sort(datos)
print("Lista ordenada:", ordenados)

#Ejemplo de salida:
#Lista ordenada: [1, 2, 3, 5, 7, 8]
# como se puede ver, la lista se ordena de menor a mayor