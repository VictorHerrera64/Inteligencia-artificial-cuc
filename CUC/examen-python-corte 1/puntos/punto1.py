# -*- coding: utf-8 -*-
"""
Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación

"""
donacion_institucion = int(input("Escriba el valor de la donación : "));
admin = donacion_institucion*0.35;
sistemas = admin*0.25;
teleco = sistemas*0.1;
restante = donacion_institucion - (admin+sistemas+teleco);
conta = donacion_institucion - restante;
print(f'Donacion  de la institucion: {donacion_institucion} \n Donacion a administracion : {admin}  \n  Donacion  a  sistemas : {sistemas} \n Donacion a telecomucion: {teleco}  \n  Donacion a contabilidad : {conta}');





