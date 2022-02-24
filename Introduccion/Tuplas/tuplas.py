#Introduccion a Tuplas ---> tuple()
#SON INMUTABLES ES NECESARIO CONVERTIRLO A LISTA
#variable = (elemento1,elemento2,elementoN)
tupla = (1,2,3,4,5,1)
print(tupla)
#indice
print(tupla[0])
#slicing (exceptua el ultimo)
print(tupla[0:2])
#longitud
print("longitud de tupla es : ",len(tupla))
#Metodos
#index(elemento) - busca y devulve el indice sino lo encuentra devuelve error
print(tupla.index(3))
#count(elemento) -  devuelve la cantidad de veces que se repite
print(tupla.count(1))
#Casting de tupla a lista y viceversa
lista = list(tupla)
print("lista convertida : ",lista)
lista.append(6)
tupla = tuple(lista)
print("Tupla convertida",tupla)
