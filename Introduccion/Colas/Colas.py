#Introduccion a Colas 
#se debe importar deque de la libreria collections
from collections import deque
#inicializacion
cola = deque() #cola vacia
cola = deque(['Hector','Miguel','Victor'])
#agregar
cola.append('Maria')
print(cola)
#sacar un elemento
cola.popleft()
print(cola)
#Eliminar elemento por su valor
cola2 = deque()
cola2 = deque([1,2,3,4,5,6])
print(cola2)
cola2.remove(1)
print(cola2)
#Invertir el orden de los elementos en deque:
cola2.reverse()
print(cola2)