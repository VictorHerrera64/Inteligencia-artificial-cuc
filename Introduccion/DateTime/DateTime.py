from datetime import datetime , timedelta

dt = datetime.now()    # Fecha y hora actual
print(dt)
print(dt.year)         # año
print(dt.month)        # mes
print(dt.day)          # día
print(dt.hour)         # hora
print(dt.minute)       # minutos
print(dt.second)       # segundos
print(dt.microsecond)  # microsegundos
#Mostrar una fecha
print(dt.strftime("%A %d %B %Y %I:%M")) # ingles por defecto
#Se debe importar modulo locale
import locale
# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES') 
print(dt.strftime("Fecha Actual : "+"%A %d de %B del %Y - %H:%M"))
#Crear fecha y hora manual
fecha_hora = datetime(2020,6,28,10,37,56)
print(fecha_hora)
#MODIFICAR 
fecha_hora = fecha_hora.replace(year=3000, hour = 11)
print(fecha_hora)
#Operaciones con fechas
fecha = datetime.now()
print(fecha.strftime("%A %d de %B del %Y - %H:%M"))
# Generamos 14 días con 4 horas y 1000 segundos de tiempo
t = timedelta(days=14, hours=4, seconds=1000)
# Lo operamos con el datetime de la fecha y hora actual
dentro_de_dos_semanas = fecha + t
print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
hace_dos_semanas = dt - t
print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
