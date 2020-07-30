# ----------------------------------------------------
# Control de errores: try ... except.... else.... finally
# Permite capturar posibles errores de ejecución de un trozo de código y dar una respuesta controlada
# ----------------------------------------------------

try:
    num1 = int(input('Dividendo: '))
    num2 = int(input('Divisor: '))

    resultado = str(num1 / num2)

except ZeroDivisionError:  # Si el error es división entre cero
    resultado = 'El divisor no puede ser cero'

except Exception:  # Si el error es otra excepción diferente a la división entre cero
    resultado = 'Hay un error'

else:  # Se ejecuta si no hay un error
    print('División correcta. El resultado es:')

finally:  # Se ejecuta siempre haya o no error
    print(resultado)
