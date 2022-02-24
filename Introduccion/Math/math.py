#introduccion al modulo math
import math
print(math.floor(3.99))  # Redondeo a la baja (suelo)
print(math.ceil(3.01))   # Redondeo al alta (techo)
#Suma todos los elementos
numeros = [0.9999999, 1, 2, 3]
suma = math.fsum(numeros) 
print(suma)
#Truncamiento
print(math.trunc(123.45))
#Potencias y Raices
print(math.pow(2, 2))  # Potencia con flotante 
print(math.sqrt(9))    # Raíz cuadrada 
#Constantes
print(math.pi)  # Constante pi
print(math.e)   # Constante e
#Funciones trigonometricas
print(math.sin(math.pi/4))   # returns 0.7071067811865476
print(math.cos(math.pi))      # returns -1.0
print(math.tan(math.pi/6))   # returns 0.5773502691896257
print(math.hypot(12,5))       # returns 13.0
