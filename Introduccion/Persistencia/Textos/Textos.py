#Persistencia con cadenas
#importar el modulo io y la funcion open
from io import open
texto = "Una línea con texto\nOtra línea con texto"
# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','w')  #escritura (write) 
# Escribimos el texto
fichero.write(texto) 
# Cerramos el fichero
fichero.close()  #importante
#----------------------------------#
fichero = open('fichero.txt','r')   # Lectura (read)
# Lectura completa
texto = fichero.read() 
# Cerramos el fichero
fichero.close()  #importante
print(texto)
#---------METODOS-------------#
#Leemos creando una lista de líneas
fichero = open('fichero.txt','r')
texto = fichero.readlines()
fichero.close()
print(texto)
#Otra forma de leer los ficheros
with open("fichero.txt", "r") as fichero:
    for linea in fichero:
        print(linea)
fichero.close()

#Agregar otra cadena
# Ruta donde leeremos el fichero, a indica extensión (puntero al final)
fichero = open('fichero.txt','a') #modo append (write)
fichero.write('\nOtra línea más abajo del todo')
fichero.close()
#----------------------------#
fichero = open('fichero.txt','r') #modo lectura   
texto = fichero.readlines()
fichero.close()
print(texto)
#--------------------------------------#
#Puntero
fichero = open('fichero.txt','r') #modo lectura
texto2 = fichero.readlines()
fichero.seek(10) #indice del caracter
texto3 = fichero.readlines()
fichero.close()
print("cadena normal")
print(texto2)
print("cadena desde el caracter 10")
print(texto3)
#----------------------------------------------#
#modificar 
fichero = open('fichero.txt','r+')
texto = fichero.readlines() #lista de la cadena
# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"
# Volvemos a ponter el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()
# Leemos el fichero de nuevo
with open("fichero.txt", "r") as fichero:
    print(fichero.read())







