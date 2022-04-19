# -*- coding: utf-8 -*-
"""
Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.
"""
sueldo_base = int(input("Digite sueldo base del vendedor : "));
cantidad_ventas = int(input("Digite cantidad de ventas realizadas : "));
ventas = []
for i in range(1, cantidad_ventas+1):
   valor =  int(input(f' Digite el valor de la venta No {i} : '));
   ganancia = valor * 0.15;
   ventas.append(ganancia);
   
total_comision = sum(ventas);
total = sueldo_base + total_comision;
print(f'Sueldo base : {sueldo_base} \n comision ganada : {total_comision} \n sueldo devengado : {total}')
   



