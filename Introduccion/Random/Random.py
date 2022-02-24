#Introduccion modulo Random
import random

# Flotante aleatorio >= 0 y < 1.0
print(random.random())      

# Flotante aleatorio >= 1 y <10.0       
print(random.uniform(1,10))

# Entero aleatorio de 0 a 9, excluído el ultimo
print(random.randrange(10))

# Entero aleatorio de 0 a 100 cada 2 números
print(random.randrange(0,101,2)) #el ultimo argumento es el salto

# Letra aleatoria
print(random.choice('Hola mundo'))

# Elemento aleatorio
print(random.choice([1,2,3,4,5]))

# Dos elementos aleatorios
print(random.sample([1,2,3,4,5], 2))

# Barajar una lista, queda guardado
lista = [1,2,3,4,5]
random.shuffle(lista) #revolver una lista
print(lista)

