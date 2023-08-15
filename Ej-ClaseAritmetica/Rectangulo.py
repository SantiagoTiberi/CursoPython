class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calcularArea(self):

        return f"Area del rectangulo: {self.base*self.altura}" 

base=int(input("Proporciona la base: "))
altura=int(input("Proporciona la altura: "))

r1 = Rectangulo(base,altura)
print(r1.calcularArea())
