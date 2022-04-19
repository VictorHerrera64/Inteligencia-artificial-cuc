# -*- coding: utf-8 -*-
"""
Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos
"""
curso = int(input("Digite total de estudiantes : "));
redes = int(input("Digite cantidad alumnos de redes : "));
conta = int(input("Digite cantidad alumnos de contabilidad : "));
dise = int(input("Digite cantidad alumnos de diseño: "));
valor_redes = (redes/curso)*100
valor_conta = (conta/curso)*100
valor_dise = (dise/curso)*100
print(f' Curso :  {curso} \n  Porcentaje estudiante redes : {valor_redes}% \n   Porcentaje estudiante contabilidad: {valor_conta}% \n Porcentaje estudiante diseño : {valor_dise}%')