# -*- coding: utf-8 -*-
"""
Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.
"""
talleres = [];
for i in range(1,4):
   nota =  int(input(f' Digite nota del taller No {i} : '));
   talleres.append(nota);

porcentaje_talleres=(sum(talleres)/3)*0.5;
examen = int(input("Digite nota de examen final : "));
proyecto = int(input("Digite nota de proyecto : "));
porcentaje_examen = examen*0.3;
porcentaje_proyeto = proyecto*0.2;
nota_final = porcentaje_talleres+porcentaje_examen+porcentaje_proyeto;
print(f' Talleres(50%) : {porcentaje_talleres} \n examen (30%) : {porcentaje_examen} \n proyecto (20%) : {porcentaje_proyeto} \n');
print(f'NOTA FINAL : {nota_final}')

