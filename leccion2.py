# ---------------------------------------------
# ESTRUCTURAS DE CONTROL EN PYTHON
#
# Operadores lógicos
#   == Igual que
#   != Distinto
#   <> Diferente
#   <  Menor que
#   >  Mayor que
#   <= Menor o igual que
#   >= Mayor o igual que
#   is Ambos lados son el mismo objeto
#   in La colección del lado derecho contiene al elemento del lado izquierdo
#
# Operadores booleanos
#   and Operador Y
#   or  Operador O
#   not Operador negación
#
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
