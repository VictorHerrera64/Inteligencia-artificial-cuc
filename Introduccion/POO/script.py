from vehiculo import *


lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)