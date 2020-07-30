import os  # Módulo con métodos que permiten borrar ficheros

# Leer ficheros de texto en python
fichero = open('./prueba.txt', 'rt')  # Modo de apertura 'rt' ==> r: read, t: texto
texto = fichero.read()  # Guarda el contenido del fichero en la variable texto de tipo str

print(texto)

# Grabar un fichero de texto
fichero = open('./prueba2.txt', 'wt')  # Modo e apertura 'wt' ==> w: write, t: texto

texto = 'Mi cadena de texto a grabar \nen el fichero creado.\n'
fichero.write(texto)  # Escribimos el contenido
fichero.close()  # Cerramos el fichero  !!! MUY IMPORTANTE !!!

# Añadir contenido a un fichero existente
fichero = open('./prueba2.txt', 'at')  # Modo e apertura 'at' ==> a: append, t: texto

texto = '\nNuevo texto a añadir.\n'
fichero.write(texto)
fichero.close()

# Borrar un fichero de texto
os.remove('./prueba2.txt')
