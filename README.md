# CamposAguado_IA_Algoritmos_de_Ordenamiento

# Algoritmos de Ordenamiento en Python

Este repositorio contiene la implementación de diversos **algoritmos de ordenamiento**, tanto **internos** como **externos**, escritos en Python 

---

## 1. ¿Qué es el ordenamiento?

El **ordenamiento** es la operación de **arreglar los elementos en algún orden secuencial**, ya sea **ascendente o descendente**, de acuerdo con un criterio determinado (números, letras, fechas, etc.).

###  Propósito:
El propósito principal es **facilitar las búsquedas** y operaciones posteriores sobre el conjunto de datos.

Ordenar significa **mover los datos o sus referencias** para que queden organizados por categorías o valores.

---

##  2. ¿Cuándo conviene usar un método de ordenamiento?

- Cuando se necesita **realizar múltiples búsquedas** en un conjunto de datos.
- Cuando **el tiempo de acceso** y respuesta es un factor importante.
- Para facilitar tareas como la comparación, clasificación, segmentación o filtrado.

---

##  3. Tipos de ordenamientos

### 3.1 Ordenamientos Internos
Se utilizan cuando **todos los datos caben en la memoria principal (RAM)**, y se pueden acceder con el mismo costo (ej. lista en Python).

### 3.2 Ordenamientos Externos
Se utilizan cuando los datos están en **memoria secundaria** (como archivos en disco), y el costo de acceso depende de su ubicación.

---

##  4. Algoritmos de ordenamiento

### 4.1  Ordenamientos Internos

| Algoritmo                   | Explicación                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------|
| **1. Insertion Sort**       | Inserta elementos en su posición correcta en una lista parcialmente ordenada.                                   |
| **2. Selection Sort**       | Selecciona el mínimo (o máximo) elemento y lo coloca en su posición. Simples pero lentos para grandes volúmenes.|
| **3. Intercambio**          | Compara elementos adyacentes y los intercambia si están en orden incorrecto. Muy básico, pero fácil de entender.|
| **4. Ordenamiento de árbol**| Inserta los elementos en un árbol binario de búsqueda y luego hace un recorrido in-order.                       |
| **5. QuickSort**            | Usa la técnica de divide y vencerás, eligiendo un pivote y dividiendo la lista en menores y mayores.            |
| **6. MergeSort**            | Divide la lista en mitades, ordena cada mitad recursivamente y luego las fusiona. Estable y eficiente.          |
| **7. RadixSort**            | Ordena números dígito a dígito, de menor a mayor dígito significativo.                                          |

---

### 4.2  Ordenamientos Externos

| Algoritmo                           | Explicación                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------|
| **1. Straight Merging**             | Divide y ordena sublistas, luego las fusiona de forma secuencial.               |
| **2. Natural Merging**              | Aprovecha runs naturales ya ordenados para fusionarlos directamente.            |
| **3. Balanced Multiway Merging**    | Usa múltiples archivos auxiliares y mezcla balanceada entre ellos.              |
| **4. Polyphase Sort**               | Variante optimizada del multiway merging que minimiza accesos al disco.         |
| **5. Distribution of Initial Runs** | Fase previa a los merges: detecta y divide secuencias ya ordenadas en los datos.|

---

##  Librerías utilizadas en los códigos

| Librería         | Función principal                                             |
|------------------|---------------------------------------------------------------|
| `heapq`          | Implementación de colas de prioridad (para mezcla eficiente). |

