#importar libreria numpy y asignarle alias 'np'
import numpy as np
# ----------------------------------------------------- #
# Creacion de arreglos 
# Vector
vector = np.array([1,2,3,4])
print(f'Vector : {vector}')
# Matriz
matriz = np.array([(1,2,3),(4,5,6)])
print(f'Matriz : {matriz}')
'''dtype: Describe cómo deben interpretarse 
los bytes en el bloque de memoria de tamaño 
fijo correspondiente a un elemento de matriz. '''
decimales = np.array([(1.4,2.3,3.1),(4.9,2.8,0.6)],dtype=float)
print(f'Matriz decimales : {decimales}')
# ----------------------------------------------------- #
# rango de arreglos n-1
lista = np.arange(10)
print(f'Lista : {lista}')
# convertir list a array numpy
vocales = ['a','e','i','o','u']
vocales_np = np.array(vocales)
print(f' lista convertida en numpy array : {vocales_np}')
# ----------------------------------------------------- #
#Arreglos  personalizados (filas - columnas)
# Matriz de ceros
ceros = np.zeros((2,3))
print(f'Matriz de ceros : {ceros}')
#Dimension variable.shape
print(f'Dimension Matriz ceros : {ceros.shape}')
# Matriz de unos
unos = np.ones((3,2))
print(f'Matriz de unos : {unos}')
#Dimension variable.shape
print(f'Dimension Matriz unos : {unos.shape}')
#Matriz de x numero especifico (dimesion),numero)
matriz = np.full((3,3),5)
print(f'Matriz de numero especifico "5" {matriz}')
# Matriz con numeros random
matriz = np.random.random((3,3))
print(f'Matriz de numero random {matriz}')
# Matriz con numeros random enteros
matriz = np.random.randint(6,size=(5,5))
print(f'Matriz de numero random enteros {matriz}')
# Matriz con numeros random decimales
matriz = np.random.uniform(0,5,size=(5,5))
print(f'Matriz de numero random decimales {matriz}')
# Matriz identidad
matriz = np.eye(5)
print(f'Matriz identidad 5x5 {matriz}')
#Matriz traspuesta
traspuesta = unos.T
print(traspuesta)
# ----------------------------------------------------- #
#Operaciones
a = [1,2,3]
b = [4,5,6]
np1 = np.array(a)
np2 = np.array(b)
np3 = np1+np2
print(np3)
np3 = np1-np2
print(np3)
np3 = np1*np2
print(np3)
np3 = np1/np2
print(np3)
#Raiz cuadrada
print(np.sqrt(np1))
#Coseno
print(np.cos(np1))
#Seno
print(np.sin(np1))
#Logaritmo
print(np.log(np1))
#Comparar
print(np1==np2)
# ----------------------------------------------------- #
'''
Ejercicio 1
 Haga un algoritmo de matriz de numeros random y que de como resultado:
Principal y el resto de numeros en 0
'''
aleatorio = np.random.random((2,2))
print(aleatorio)
identidad = np.eye(2)
resultante = aleatorio*identidad
print(resultante)
# ----------------------------------------------------- #
#Funciones agregadas
#Elemento mayor
print(aleatorio.max())
#Elemento menor
print(aleatorio.min())
#Promedio
print(aleatorio.mean())
#Sumatoria
print(aleatorio.sum())
# ----------------------------------------------------- #
#Filtrado
c = [[1,2,3],[4,5,6],[7,8,9]]
npc= np.array(c)
print(npc)
#menos que x numero
print(npc[npc<5])
#Solo fila 1
print(npc[1,:])
# ----------------------------------------------------- #
'''
Ejercicio 2
 Haga un algoritmo que de 49 notas aleatorias muestre 
 las notas por encima del promedio
'''
notas = np.random.uniform(0,5, size=(7,7))
promedio=notas.mean()
print(notas[notas>promedio])





