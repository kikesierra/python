# Listas son colecciones de elementos ordenados. Se representan entre corchetes
colores = ['rojo', 'verde', 'amarillo']

# Se accede a los elementos por su posición, enpezando en 0
print(colores[0])

# Se puede cambiar los elementos de la lista
colores[0] = 'azul'

len(colores)  # Devuelve el número de elementos de la lista

colores.append('naranja')  # Añade un elemento nuevo al final de la lista

# Borrar valores
colores.remove('verde')
colores.clear()  # Borra todos los elementos de la lista

# Recorrer una lista con un blucle
for color in colores:
    print(color)


# Tuplas: Colección de elementos ordenada que no se puede modificar. 
# Se representa entre paréntesis
# Funciona igual que las listas, salvo que no puede añadirse, eliminarse ni modificarse su contenido
tupla_frutas = ('pera', 'uva', 'fresa')

# Conjunto: Colección de elementos desordenados, es decir, no tiene un indice
# Se puede hacer las mismas operaciones que con las listas
# Se representa entre llaves
conjunto_colores = {'rojo', 'verde', 'azul'}

# No se puede acceder a un elemento con nombre[i] 

# Añadir elementos
conjunto_colores.add('negro')

# Eliminar un elemento indicando el nombre
conjunto_colores.remove('verde')

# Diccionarios: Colección de elementos indexados que no están ordenados y que se pueden modificar
# Se representan entre llaves y cada elemento es un par clave:valor
dicc_colores = {'red': 'rojo', 'blue': 'azul', 'black': 'negro'}
print(dicc_colores)

# Se accede a los elementos por su clave
color = dicc_colores['red']
print(color)

# Añadir elementos al diccionario
dicc_colores['yellow'] = 'amarillo'

print(dicc_colores)

# Borrar valores
dicc_colores.pop('yellow')
print(dicc_colores)

del(dicc_colores['black'])
print(dicc_colores)

# Imprimir las claves del diccionario
print('Claves del diccionario: ')
for color in dicc_colores:
    print(color)

# Imprimir las claves y los valores del diccionario
print('Claves y valor del diccionario:')
for (clave, valor) in dicc_colores.items():
    print(clave, valor)
