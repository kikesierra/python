# ---------------------------------------------------
# CLASES Y OBJETOS
# ---------------------------------------------------

# Definición de una clase sencilla con dos atributos
class Persona:
    nombre = 'Juan'
    edad = 30


# Definición de un objeto
persona1 = Persona()
print(f'Datos de la persona ==> Nombre: {persona1.nombre} Edad: {persona1.edad}')

# Modificar los atributos de un objeto
persona1.nombre = 'Kike'
persona1.edad = 52
print(f'Datos de la persona ==> Nombre: {persona1.nombre} Edad: {persona1.edad}')


# Definición de una clase con un constructor
class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print(f"""Marca: {self.marca} \nColor: {self.color} \nCombustible: {self.combustible} \nCilindrada: {self.cilindrada}""")


coche1 = Coche('BMW', 'Azul', 'Gasoil', 2400)
coche1.mostrar_caracteristicas()

