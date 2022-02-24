# Introduccion a diccionarios ---> Dict()
# Son arreglos asosiativos y colecciones desordenadas
# inicializacion
# variable = {clave : valor}
colores = {"amarillo": "yellow", "rojo": "red", "verde": "green", "morado": "purple"}
print(colores)
# acceder por las claves
print(colores['amarillo'])
# borrar
del(colores['amarillo'])
print(colores)
# modificar valores
edades = {"Victor": 20, "Daniela": 17, "Liliana": 47}
edades['Victor'] += 1
print(edades)
# mostrar por ciclo for
for claves, valores in edades.items():
    print(claves, ":", valores)
# eliminar todo
edades.clear()
print(edades)
# copiar todos los elementos
numeros = {"uno": "one", "dos": "two", "tres": "three"}
copia = numeros.copy()
print(copia)
# Concatenar dos diccionarios
diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talla": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2)
print(diccionario1)
# Establecer una clave y valor por defecto
camisa = {"color": "rosa", "marca": "Zara"}
clave = camisa.setdefault("talla", "M")
print(camisa)
# obtener solo las claves
claves = camisa.keys()
print(claves)
# obtener solo los valores
valores = camisa.values()
print(valores)
# longitud de un diccioario
print(len(camisa))
