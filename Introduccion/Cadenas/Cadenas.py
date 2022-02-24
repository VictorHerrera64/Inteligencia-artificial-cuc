# Introduccion a cadenas  --->  str()
# Truco: para colocar algo entre comillas
print("Esta \"palabra\" se encuentra entre comillas dobles")
# Truco: para colocar algo entre comillas simples
print("Esta letra \'a\' se encuentra entre comillas simples")
# Mostrar en crudo
print(r"C:\usario\Directorio")
#(indices en cadenas) Hacer referencia a un caracter de una cadena
Cadena = "Python"
print(Cadena, ":", Cadena[0])
# Slicing
# Cadena[Inicio:Fin] (se excluye el ultimo)
print(Cadena, ":", Cadena[0:2])
# Longitud de cadena
print("La palabra \"Python\" tiene ", len(Cadena), " caracteres")
# Mayusculas
print("palabra en Mayusculas : ", Cadena.upper())
# Minusculas
print("palabra en Minusculas : ", Cadena.lower())
# Mayuscula inicial
print("palabra en Mayusculas incial : ", Cadena.capitalize())
# Mayuscula inicial en cada palabra
Cadena2 = "hola mundo"
print("palabra en Mayusculas en cada palabra : ", Cadena2.title())
# Contar el numero de veces de un caracter o palabra
print("la letra \'o\' se encuentra en la cadena", Cadena2.count('o'), "veces")
# El indice de cuando empieza una palabra
print("la palabra \"mundo\" empieza en la cadena en el indice", Cadena2.find('mundo'))
# busqueda en reversa del indice de cuenta empieza una palabra
Cadena3 = "hola mundo mundo3"
print("la ultima palabra \"mundo\" empieza en la cadena en el indice", Cadena3.rfind('mundo'))
# Preguntar si es un numero
n = "100"
print(n, "Es un numero? ", n.isdigit())
# Preguntar si es alfanumerico
alfanumerico = "VICTOR HERRERA"
print(alfanumerico, "Es alfanumerico? ", alfanumerico.isalnum())
# preguntar si tiene solo letras del alfabeto (no incluye espacio)
palabra = "Victor"
print(palabra, "tiene solo letras? ", palabra.isalpha())
# preguntar si esta en Minuscula, Mayuscula, etc ...
print(Cadena2, "es Minuscula? ", Cadena2.islower())
print(Cadena2, "es Mayuscula? ", Cadena2.isupper())
# preguntar si solo es espacio
print(Cadena2, "solo tiene espacios? ", Cadena2.isspace())
# preguntar si una cadena empieza por un caracter o palabra
print(Cadena2, "empieza por \'H\'? ", Cadena2.startswith('h'))
# preguntar si una cadena termina por un caracter o palabra
print(Cadena2, "termina por \'o\'? ", Cadena2.endswith('o'))
# separar cada palabra por comas
print("cadena separada por comas ", Cadena3.split())
# separar cade caracter de una palabra por comas
print(Cadena3, ",".join(Cadena3))
# separar cade caracter de una palabra por espacios
print(Cadena3, " ".join(Cadena3))
# reemplazar algo de la cadena
# cadena.replace(sustituir,sustito)
print(Cadena3, Cadena3.replace('o', '0'))
# cadena.replace(sustituir,sustito,cantidad de veces)
Cadena4 = "Hola mundo mundo mundo"
print(Cadena3, Cadena4.replace('mundo', '', 2))
# Truco para concatenar variables
print("Mis cadenas: \n {} \n {} \n {} \n {}".format(Cadena, Cadena2, Cadena3, Cadena4))
