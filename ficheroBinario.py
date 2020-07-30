# -----------------------------------------------------------
# FICHEROS BINARIOS: módulo pickle
# Permite almacenar estructuras como listas, tuplas, diccionarios, etc... en ficheros binarios
# que pueden recuperarse de nuevo manteniendo la estructura original
# ------------------------------------------------------------
import pickle  # Módulo para usar ficheros binarios

colores = ['azul', 'rojo', 'verde', 'azul']  # Lista de colores

# Grabar un fichero binario
fichero = open('./fichero_colores.pckl','wb')  # Abrimos un fichero binario en formato pickle

pickle.dump(colores, fichero)

fichero.close()

# Leer un fichero binario
fichero = open('./fichero_colores.pckl', 'rb')

lista = pickle.load(fichero)
print(lista)
fichero.close()

# Ejemplo de uso de pickle con un diccionario
frutas = {'manzana': 'apple', 'naranja': 'orange', 'platano': 'banana', 'limón': 'lemon'}

# Se crea el fichero binario con el contenido del diccionario
fichero = open('./datos/frutas.pckl', 'wb')
pickle.dump(frutas, fichero)
fichero.close()

# Leemos el diccionario del fichero
fichero = open('./datos/frutas.pckl', 'rb')
mis_frutas = pickle.load(fichero)
fichero.close()

# Mostrar los valores del diccionario
print(mis_frutas.values())

# Mostrar el diccionario leído
for codigo, valor in mis_frutas.items():
    print(f'La fruta {codigo} en inglés se llama {valor}')

# O de otra forma
for fruta in mis_frutas:
    print(f'{mis_frutas[fruta]} es el nombre inglés de {fruta}')
