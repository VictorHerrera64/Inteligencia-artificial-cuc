#Introduccion a Excepciones
#Declaracion
#try:
   #Codigo (lo que se va ejecutar) 
#except (Tipo de error)(opcional):
   # print("Ha ocurrido un error") #se lanza la excepcion
#Ejemplo
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien (por el ciclo)
    finally: #(opcional)
        print("Fin de la iteración") # Siempre se ejecuta
#Ejemplo 2 
try:
    n = int(input("Introduce un número: "))
    r = 5/n
    print("{}/{} = {}".format(5,n,r))
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__) #Nos dice que tipo de error es!
else:
	print("Todo ha funcionado correctamente")
