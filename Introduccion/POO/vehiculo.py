class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo): #HERENCIA

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada)




class Camioneta(Coche): #HERENCIA

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada) 


# def catalogar(vehiculos):
#    for v in vehiculos:
#        print(type(v).__name__, v)

def catalogar(vehiculos, ruedas=None):

    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas: 
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)





