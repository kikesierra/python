import modulo1

# Crear un objeto Coche
coche1 = modulo1.Coche('BMW', 'Azul', 'Gasoil', 2.5)

# Mostrar las caracteristicas
coche1.mostrar_caracteristicas()

# Calcular la media de dos numeros con la función lamda del módulo
resultado = modulo1.media(100, 50)
print('La media es {}'.format(resultado))
