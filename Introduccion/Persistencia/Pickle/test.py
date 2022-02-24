from ejemplo2 import *
# Creamos un catálogo
c = Catalogo()
# Agregamos unas películas
c.agregar( Pelicula("El Padrino", 175, 1972) )
c.agregar( Pelicula("El Padrino: Parte 2", 202, 1974) )
# Mostramos el catálogo de nuevo
c.mostrar()
# Borramos el catálogo de la memoria ram (persistirá el fichero)
del(c)
#------------------------------------#
#Creamos un catálogo
c = Catalogo()
# Agregamos otra  película
c.agregar( Pelicula("Prueba", 100, 2005) )

# Mostramos el catálogo de nuevo
c.mostrar()