# Programa que importa módulos completos
import misfunciones  # Se importa el módulo indicando el nombre del archivo

misfunciones.saludar('Kike')

nombre = input('Dime tu nombre: ')
misfunciones.saludar(nombre)
misfunciones.despedirse(nombre)
