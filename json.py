# ----------------------------------------
# JSON: Formato de intercambio de información en formato texto
# ----------------------------------------
import json5

# Convertir un dicccionario a JSON
producto1 = {'nombre': 'silla', 'color': 'blanco', 'precio': 200}

# Convierte el diccionario a un json (en formato texto)
texto_json = json5.dumps(producto1)

# El diccionario como texto
print('El diccionario en formato texto: {}'.format(texto_json))

print('Tipo de texto_json: {}'.format(type(texto_json)))  # El tipo es str
print('Tipo de producto1: {}'.format(type(producto1)))  # El tipo es dict

# Transforma un texto JSON en un objeto
nuevo_diccionario = json5.loads(texto_json)

# Mostramos el contenido del diccionario y su tipo
print(nuevo_diccionario)
print(type(nuevo_diccionario))

# Convertir una lista a JSON
colores = ['rojo', 'verde', 'azul']

texto = json5.dumps(colores)

print(texto)
print(type(colores))
print(type(texto))
