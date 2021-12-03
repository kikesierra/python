import misfunciones

# Capturamos tres número por pantalla
try:
    num1 = input('Primer número: ')
    num2 = input('Segundo número: ')
    num3 = input('Tercer número: ')

    resultado = misfunciones.operacion(float(num1), float(num2), float(num3))

except ZeroDivisionError:
    resultado = 'No se puede dividir entre cero'

except Exception:
    resultado = 'Alguno de los datos introducidos no es un número'

else:
    print('El resultado de la operación es:')

finally:
    print('{r:1.2f}'.format(r=resultado))  # Resultado con dos decimales
