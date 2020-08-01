# Uso de fechas y horas en Python
from datetime import datetime  # Importamos la clase datetime

ahora = datetime.now()
print(ahora)

# Obtener los datos por separado
print('Son las {} horas, {} minutos, del {} de {} de {}'.format(ahora.hour, ahora.minute, ahora.day, ahora.month, ahora.year))

# Dar formato a la fecha
fecha = ahora.strftime('%d-%m-%Y')  # Dia, mes y año con 4 dígitos
print(fecha)

# Crear un objeto de tipo fecha-hora
fecha = datetime(1968, 8, 15)
print(fecha)
