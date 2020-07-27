#
#Conceptos básicos de Pyhon
#

#Tipos de variables (int, float, str, bool)
vEntero = 2 #Variable de tipo int
vDecimal = 2.5 #Variable de tipo float
vCadena1 = "Texto" #Variable de tipos str con comillas dosbles
vCadena2 = 'Otro texto' #Variable de tipos str con comillas simples
vCadena3 = """Otro texto largo con caracteres especiales
              espacios
              y saltos de linea""" #Variable de tipos str con comillas triples
vResultadoT = True #Variable de tipo bool
vResultadoF = False 
vLista1 = [1,2,3,4] #Lista de números enteros
vLista2 = [1, 2.5, 'Texto', True, [1,2]] #Lista de valores de tipos diferentes

#Operaciones aritméticas
suma = vEntero + vDecimal
resta = vDecimal - vEntero
producto = vEntero * vDecimal
potencia = vDecimal ** vEntero
divisionP = vDecimal / vEntero #División precisa
divisionE = vDecimal // vEntero #División entera
resto = vDecimal % vEntero #Resto de la división

#Operaciones con cadenas
concatena = vCadena1 + vCadena2 #Une las cadenas
longitud = len(vCadena1) #Longitud de la cadena
minusculas = vCadena1.lower() #Devuelve la cadena en minúsculas
mayusculas = vCadena1.upper() #Devuelve la cadena en mayúsculas


