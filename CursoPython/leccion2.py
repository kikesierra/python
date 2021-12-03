# ---------------------------------------------
# ESTRUCTURAS DE CONTROL EN PYTHON
#
# Operadores de asignación
#   = Asigna al objeto de la izquierda el de la derecha
#   += Suma el valor de la parte derecha y lo asigna (a += b ==> a = a + b)
#   -= Resta el valor de la parte derecha y lo asigna (a -= b ==> a = a - b)
#   *= Multiplica el valor de la parte derecha y lo asigna (a *= b ==> a = a * b)
#   /= Divide el valor de la parte derecha y lo asigna (a /= b ==> a = a / b)
#   **= Potencia el valor de la parte derecha y lo asigna (a **= b ==> a = a ** b)
#
# Operadores de comparación
#   == Igual que
#   != Distinto
#   <> Diferente
#   <  Menor que
#   >  Mayor que
#   <= Menor o igual que
#   >= Mayor o igual que
#
# Operadores lógicos
#   and Operador Y
#   or  Operador O
#   not Operador negación
#
# Operadores de identidad
#   is Ambos lados son el mismo objeto
#   is not Los objetos de ambos lados son diferentes
#
frutas1 = ['peras', 'manzanas']
frutas2 = ['peras', 'manzanas']
frutas3 = frutas1

resultado = frutas1 is frutas2  # Devolverá False
resultado = frutas1 is frutas3  # Devolverá True

# Operadores de pertenencia
#   in La colección del lado derecho contiene al elemento del lado izquierdo
#   not in La colección no contiene al elemento del lado izquierdo
resultado = 'peras' in frutas1  # Devuelve True
resultado = 'naranjas' in frutas2  # Devuelve False
resultado = 'peras' not in frutas2  # Devuelve False
resultado = 'naranjas' not in frutas2  # Devuelve True

# Expresión condicional
#    if expresion1:
#       sentencias
#    elif expresion2:
#       sentencias
#    else:
#       sentencias
#
# Bucles
#    while expresion1:
#       sentencias
#
#    for expresion1 in range(ini, fin):
#       sentencias
#
# ---------------------------------------------

# Obtenemos una cadena de texto por entrada
# Si su longitud <= 10 se imprime caracter a caracter
# Si su longitud > 10 y <= 20 se imprime en trozos de dos caracteres
# Si su longitud > 20 se imprime en trozos de tres caracteres

vCadena = input('Introduce un texto: ')
vCadena2 = vCadena
vLongitud = len(vCadena)

if vLongitud <= 10:
    print('La longitud es <= 10. Caracteres de la cadena:')
    while len(vCadena) > 0:
        print(vCadena[0:1])
        vCadena = vCadena[1:]

elif vLongitud <= 20:
    print('La longitud es > 10 y <= 20. Caracteres de la cadena:')
    while len(vCadena) > 0:
        print(vCadena[0:2])
        vCadena = vCadena[2:]
else:
    print('La longitud es >30. Caracteres de la cadena:')
    while len(vCadena) > 0:
        print(vCadena[0:3])
        vCadena = vCadena[3:]

# Da la vuelta a la cadena
print('\nImprimiendo la cadena al revés:')
for i in range(1, len(vCadena2)+1):
    print(vCadena2[-i])

# Bucle for sobre un objeto iterable
lista = ['Enrique', ['Sierra', 'Blanco'], 52, 182, 79.5]
for i in lista:
    print(i)

diccionario = {'Nombre': 'Enrique', 'Apellidos': ['Sierra', 'Blanco'], 'Edad': 52, 'Altura': 182, 'Peso': 79.5}
for i in diccionario:
    print(i, ':', diccionario[i])  # Imprime la etiqueta y el valor de cada etiqueta
    print(f'{i}: {diccionario[i]}')
