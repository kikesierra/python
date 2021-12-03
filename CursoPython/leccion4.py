# ------------------------------------------------
# FUNCIONES
# ------------------------------------------------

# Función sin parámteros y sin devolver resultado
def miFuncion():
    print('No sirvo para nada')

# Función con parámetros
def calculadora(p1, p2, p3):
    if p3 == '+':
        print('La suma es {}'.format(p1 + p2))
    elif p3 == '-':
        print('La resta es {}'.format(p1 - p2))
    else:
        print('No se hacer esa operación')


calculadora(2, 3, '+')
calculadora(100, 20, '-')
calculadora(2, 4, '*')


# Funciones con retorno de valor
def media(v1, v2):
    return (v1 + v2) / 2


resultado = media(100, 20)
print(f'La media es {resultado}')


# Las listas, conjuntos y diccionarios se pasan por referencia
def creaColor(pColor, pColores):
    pColores.append(pColor)


colores = []
color = input('Añade un color: ')
creaColor(color, colores)
color2 = input('Añade otro color: ')
creaColor(color2, colores)
print('Tus colores son {}'.format(colores))


# Funciones lambda
# Son pequeñas funciones que no tienen nombre. Se definen asignándola a una variable
media = lambda p1, p2: (p1 + p2) / 2

print(f'Función lambda para calcular la media {media(12, 3)}')
