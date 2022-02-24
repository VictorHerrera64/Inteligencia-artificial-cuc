#Introduccion a listas ---> list()
# variable = [] (lista vacia)
lista = [1,2,"tres",3.5,"cuatro"]
print(lista)
#datos por indice
print(lista[0]) #muestra el primero
#datos por slicing
print(lista[0:-1]) #primero hasta el penultimo
#asignacion por indice
#variable[indice] = elemento
l1 = [1,2,4]
l1[2] = 3
print(l1)
#asignacion por slicing
letras = ['a','b','c','d','e']
letras[:3] = ['A','B','C']
print(letras)
#listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
resultante = [a,b,c]
#posicion lista - poscion de elemento de la lista
print(resultante[0][-1])
print(resultante[1][-1])
print(resultante[2][-1])
#Metodos de listas
#append(elemento) - agregar al final
l1.append(4)
print(l1)
#clear - borrar todos los elementos
l1.clear()
print(l1)
#extend(lista) - unir dos listas
l2 = [1,2,3]
l3 = [4,5,6]
l2.extend(l3)
print(l2)
#extend(elemento) - contar la cantidad de veces un elemento
l4 = [1,1,2,3,2,5,4,3]
print(l4.count(3))
#index(elemento)- el indice de un elemento de la lista
print(l4.index(1))
#insert(posicion,elemento) -agregar en x
l2.insert(0,0)
print(l2)
#pop() - sacar un elemento el ultimo elemento
l3.pop()
print(l3)
#pop(indice) - saca el elemento del indice
l2.pop(0)
print(l2)
#remove(elemento) - eliminar un elemento
l4.remove(4)
print(l4)
#reverse - voltear una lista
l4.reverse()
print(l4)
#sort -  ordenar lista
l4.sort()
print(l4)
#sort(reverse = True) - ordenar de mayor a menor
l4.sort(reverse = True)
print(l4)
#casting de tupla a lista
tupla = (1,2,3,4,5)
print(tupla)
lista = list(tupla)
print(lista)




