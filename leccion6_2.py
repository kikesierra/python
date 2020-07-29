# Programa que importa funciones de un módulos
from misfunciones import saludar  # Se importa solo la función saludar

# Para usar la función ya no se usa el nombre dle módulo, sólo el de la función
saludar('Kike')

nombre = input('Dime tu nombre: ')
saludar(nombre)
