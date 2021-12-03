# ----------------------------
# EXPRESIONES REGULARES:
# Son cadenas de texto de códigos que permiten localizar patrones
# dentro de un texto. Hay varios métodos:
#   - search: busca un patrón dentro de una cadena
#   - findall: busca todas las ocurrencias de una cadena
# ---------------------------------------------

import re  # Módluo para trabajar con expresiones regulares

texto = 'Hola, Hola, mi nombre es KikeSierra'
patron = 'nombre'

# search: Busca el patron en la cadena de texto.
# Si lo encuentra, devuelve un objeto de tipo Match
# Si no lo encuentra no devuelve nada

resultado = re.search(patron, texto)
if (resultado):
    print('Cadena encontrada')
else:
    print('No encontrado')

# Se puede usar comodines para mayor precisión
# Por ejemplo:
#    - el patrón '$' indica que el texto buscado sea el final
#    - el patrón '^' indica que el texto buscado esté al principio
#    - el patrón '.' indica un único caracter
#    - el patrón '.*' indica cualquier número de caracteres

# Buscar un texto al final de la cadena
patron = 'Kike$'

# Se puede colocar una r delante para indicar que es un patrón
# Es recomendable cuando el patrón tiene caracteres especiales
patron = r'Kike$'
if (re.search(patron, texto)):
    print('Kike está al final')
else:
    print('No está al final')

# Buscar un texto al principio de la cadena
patron = '^Hola'
if (re.search(patron, texto)):
    print('Hola está al principio')
else:
    print('No está al principio')

# Buscar varias palabras o textos
patron = 'mi.*es'  # Tiene que tener las palabras mi y es en ese orden
if (re.search(patron, texto)):
    print('Contiene las palabras buscadas')
else:
    print('No contiene las palabras buscadas')

# findall: Devuelve una lista con todas las ocurrencias encontradas
# Devuelve una lista con las ocurrencias encontradas
# Si no encuentra nada devuelve una lista vacía
texto = """El coche de Luis es rojo,
el coche de Antonio es blanco,
el coche de Silvia es rojo"""

resultado = re.findall('coche.*rojo', texto)
print(resultado)

# split:Divide una cadena a partir de un patrón
# Devuelve una lista con cada parte obtenida al dividir
# El texto del patrón se elimina del resultado

# Un uso típico es con el patrón '\s'  que representa un espacio en blanco
# Divide eltexto en las palabras que lo forman
resultado = re.split(r'\s', texto)
print(resultado)

# Divide por una coma y salto de linea
resultado = re.split(r',\n', texto)
print(resultado)

# Divide por el texto 'el '
# Tener en cuenta que 'El ' es diferente de 'el '
resultado = re.split(r'el ', texto)
print(resultado)

# sub: Sustituye todas las coincidencias de una cadena
# Primero se indica el texto a reemplazar y después elque reemplaza
# Sustituye el texto 'rojo' por 'BLANCO' en la cadena texto
resultado = re.sub('rojo', 'BLANCO', texto)
print(resultado)
