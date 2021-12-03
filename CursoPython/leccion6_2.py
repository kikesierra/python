# Programa que importa funciones de un módulos
from misfunciones import saludar  # Se importa solo la función saludar

# Se puede importar una función de un módulo y renombrarla (alias)
from misfunciones import despedirse as adios

# Para usar la función ya no se usa el nombre dle módulo, sólo el de la función
saludar('Kike')

nombre = input('Dime tu nombre: ')
saludar(nombre)

# Llamar a la función importada con el alias
adios(nombre)
