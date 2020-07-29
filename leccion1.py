# ---------------------------#
# Conceptos básicos de Pyhon #
# ---------------------------#

# Tipos de variables (int, float, str, bool)
vSinTipo = None  # Variable sin valor asignado y por lo tanto sin tipo conocido
vEntero = 2  # Variable de tipo int
vDecimal = 2.5  # Variable de tipo float
vCadena1 = "Texto"  # Variable de tipos str con comillas dosbles
vCadena2 = 'Otro texto'  # Variable de tipos str con comillas simples
vCadena3 = """Otro texto largo con caracteres especiales,'", tabuladores
              espacios y
              saltos de linea"""  # Variable de tipos str con comillas triples

print(vCadena3)

vResultadoT = True  # Variable de tipo bool
vResultadoF = False
vLista1 = [1, 2, 3, 4]  # Lista de números enteros
vLista2 = [1, 2.5, 'Texto', True, [1, 2]]  # Lista de valores de tipos diferentes

# Operaciones aritméticas
suma = vEntero + vDecimal
resta = vDecimal - vEntero
producto = vEntero * vDecimal
potencia = vDecimal ** vEntero
divisionP = vDecimal / vEntero  # División precisa
divisionE = vDecimal // vEntero  # División entera
resto = vDecimal % vEntero  # Resto de la división

# Operaciones con cadenas
concatena = vCadena1 + vCadena2  # Une las cadenas
longitud = len(vCadena1)  # Longitud de la cadena
minusculas = vCadena1.lower()  # Devuelve la cadena en minúsculas
mayusculas = vCadena1.upper()  # Devuelve la cadena en mayúsculas
tokeniza = vCadena1.split()  # Devuelve una lista con las palabras de la cadena
concatena = vCadena1 * 4  # Concatena 4 veces la cadena1

# Obtener partes de una cadena
trozo = vCadena2[0]  # Obtiene el primer caracter de lacadena
trozo = vCadena2[-1]  # Obtiene el último caracter de la cadena
trozo = vCadena2[1:3]  # Obtiene desde la posición 1 hasta la 3
trozo = vCadena2[3:]  # Obtiene desde la posición 3 hasta el final de la cadena
trozo = vCadena2[:5]  # Obtiene desde el principio hasta la posición 5


primerCaracter = vCadena1[0]  # Se puede recorrer la cadena de 0 a len-1
ultimoCaracter = vCadena1[-1]  # Se recorre la cadena al reves: -1, -2, -3,....

# Capturar entrada de teclado - Siempre se recoge como str
entrada1 = input()
entrada2 = input('Dime tu nombre: ')  # Indicando un mensaje previo

# Ejemplos de Salida por pantalla
# Salida sencilla
print(entrada1)

# Salida con texto fijo
print("El valor de la variable entrada es: ", entrada1)

# Salida con varios textos y variables separadas por comas
print("Entrada 1: ", entrada1, " - Entrada 2: ", entrada2)

# Salida usando la opción f y las variables entre corchetes
print(f'La variable entrada 1 es {entrada1} y la variable entrada 2 es {entrada2}')

# Forma alternativa de usar el format
print('La variable entrada1 es {} y la variable entrada2 es {}'.format(entrada1, entrada2))

# Usando el format para dar formato a números
numero = 1300 / 3
print('El número sin formato es {_1}'.format(_1=numero))
print('El número con formato es {v:1.2f}'.format(v=numero))  # Parte entera y dos decimales

# Obtener el tipo de una variable
print(f"""Mis variables son de los siguientes tipos:
         vSinTipo    = {type(vSinTipo)}
         vEntero     = {type(vEntero)}
         vDecimal    = {type(vDecimal)}
         vCadena1    = {type(vCadena1)}
         vLista1     = {type(vLista1)}
         vResultadoT = {type(vResultadoT)}""")

# Convertir las entradas de teclado (de tipo str) al tipo deseado (int, float)
edad = input('Dime tu edad: ')
edad = int(edad)

peso = input('Dime tu peso: ')
peso = float(peso)

# Funciones sobre cadenas
cadena = input('Dime tu nombre y apellidos: ')
cadenaL = cadena.split()  # Devuelve una lista con las palabras de la cadena
print(cadenaL)

# Split admite el caracter separador de las palabras
cadena = 'SIERRA*BLANCO*ENRIQUE'
print(cadena.split('*'))
