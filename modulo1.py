class Coche:
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print(f"""Marca: {self.marca} \nColor: {self.color} \nCombustible: {self.combustible} \nCilindrada: {self.cilindrada}""")

media = lambda p1, p2: (p1 + p2) / 2

