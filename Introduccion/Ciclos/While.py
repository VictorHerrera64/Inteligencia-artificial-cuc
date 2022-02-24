#introduccion a Ciclo While
#while condicion : (la condicion debe ser verdadera para que se ejecute)
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1

c = 0
while c <= 5:
    c+=1
    if c==3 or c==4:
        # print("Continuamos con la siguiente iteración", c)
        continue # saltarse esa interacion
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)

