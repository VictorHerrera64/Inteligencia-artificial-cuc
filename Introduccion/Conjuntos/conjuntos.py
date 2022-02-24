#introduccion a conjuntos ---> set()
#Son colecciones desordenadas de elementos unicos (no se repiten datos)
#inicializacion
conjunto = set() 
conjunto = {1,2,3,4}
print(conjunto)
#Metodos
#add(elemento)- Agregar un dato
conjunto.add(5)
print(conjunto)
#Si se encuentra en el conjunto
r = 5 in conjunto
print(5, "se encuentra en el conjunto? ",r)
#No se encuentra en el conjunto
r2 = 6 not in conjunto
print(6, "no se encuentra en el conjunto?",r2)
#cast lista a conjunto para eliminar repetidos
lista = [1,2,3,3,4,2,1,5]
lista = list(set(lista))
print(lista)
#cadena a conjunto
cadena = "VictorHerreraVictor"
c = set(cadena)
print(c)

