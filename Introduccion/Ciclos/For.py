#Introducion ciclo For
#Recorriendo listas
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:  # Para [variable] en [lista]
    print(numero)


#modificando elementos con ciclo for
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# indice = iterable , numero = inicio, enumerate(lo que se va recorrer)
for indice,numero in enumerate(numeros2):
    numeros2[indice] *= 10
print(numeros2)

#usando range() exceptua el ultimo numero '10'
for i in range(10):
    print(i)



