import moduloFicheros

fichero = moduloFicheros.Fichero('./datos/prueba3.txt')

fichero.grabar_fichero()
fichero.incluir_fichero('Mi primer texto')
print(fichero.leer_fichero())
