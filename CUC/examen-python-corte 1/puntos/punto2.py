# -*- coding: utf-8 -*-
"""
Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.
"""
inversion = int(input("Digite la inversion total : "));
p1 = int(input("Digite inversion de persona 1 : "));
p2 = int(input("Digite inversion de persona 2 : "));
p3 = int(input("Digite inversion de persona 3 : "));
valor_p1 = (p1/inversion)*100
valor_p2 = (p2/inversion)*100
valor_p3 = (p3/inversion)*100
print(f' inversion total :  {inversion} \n  Porcentaje invertido Persona 1 : {p1}% \n   Porcentaje invertido Persona 2 : {p2}% \n Porcentaje invertido Persona 3 : {p3}%')


