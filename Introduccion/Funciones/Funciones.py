#introduccion funciones
#def nombreDeLaFuncion(Argumentos):
def suma(n1,n2):
	return n1+n2 
print("Suma : ",suma(1,3))
def resta(n1,n2):
	return n1-n2 
print("Resta : ",resta(1,3))

#funcion recursiva 
def cuenta_regresiva(segundos):
	segundos -=1
	if segundos >= 0 :
		print(segundos)
		cuenta_regresiva(segundos)
	else:
		print("BOOOM!")
print(cuenta_regresiva(10))