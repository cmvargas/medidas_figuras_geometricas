import sys

class Rectangulo:
    def area(self, base, altura):
        resultado = base * altura
        print("El area es {0}".format(resultado))
    def perimetro(self, base, altura):
        resultado = base+base+ altura +altura
        print("El perimetro es {0}".format(resultado))
    def diagonal(self,base, altura):
        resultado_base = base*base
        resultado_altura = altura*altura
        resultado = (resultado_base+resultado_altura) ** (1/2)
        print("La diagonal es {0}".format(resultado))
    def opciones(self):
        text = "Opciones para calcular:\n 1. Area \n2. Perimetro \n3. Diagonal \n0. Salir\n"
        numero = int(input(text))
        if numero ==0:
            sys.exit()
        base = int(input("Digite la base:\n"))
        altura = int(input("Digite la altura:\n"))
        return numero, base, altura
    def principal(self):
        numero = 4
        while numero !=0:
            numero, base, altura = self.opciones()
            if numero == 1:
                self.area(base, altura)
            elif numero ==2:
                self.perimetro(base, altura)
            elif numero ==3:
                self.diagonal(base, altura)
            elif numero ==0:
                sys.exit()
            elif numero not in [0,1,2,3]:
                sys.exit()
class Cilindro:
    def medidas(self, base, altura, radio):
        pi = 3.141592654
        resultado_area = pi * (radio **(2)) 
        resultado_volumen = resultado_area*altura
        print("El area de la base es de {0} unidades al cuadrado\n".format(resultado_area))
        print("El volumen es de {0} unidades al cubo\n".format(resultado_volumen))

    def opciones(self):
        text = "Opciones :\n 1. Calcular medidas \n0. Salir\n"
        numero = int(input(text))
        if numero ==0:
            sys.exit()
        base = int(input("Digite la base:\n"))
        altura = int(input("Digite la altura:\n"))
        radio = int(input("Digite el radio:\n"))
        return numero, base, altura, radio
    def principal(self):
        numero = 4
        while numero !=0:
            numero, base, altura, radio = self.opciones()
            if numero == 1:
                self.medidas(base, altura, radio)
            elif numero ==0:
                sys.exit()
            elif numero not in [0,1]:
                sys.exit()
class Triangulo:
    def medidas(self, base, altura):
        resultado = (1/2) * (base*altura)
        print("El area del triangulo es de {0} unidades al cuadrado\n".format(resultado))
    def opciones(self):
        text = "Opciones :\n 1. Calcular medidas \n0. Salir\n"
        numero = int(input(text))
        if numero ==0:
            sys.exit()
        base = int(input("Digite la base:\n"))
        altura = int(input("Digite la altura:\n"))
        return numero, base, altura
    def principal(self):
        numero = 4
        while numero !=0:
            numero, base, altura = self.opciones()
            if numero == 1:
                self.medidas(base, altura)
            elif numero ==0:
                sys.exit()
            elif numero not in [0,1]:
                sys.exit()

class Cubo: 
    def medidas(self, lado):
        resultado = lado*lado*lado
        print("El volumen del cubo  es de {0} unidades al cubo\n".format(resultado))
    def opciones(self):
        text = "Opciones :\n 1. Calcular medidas \n0. Salir\n"
        numero = int(input(text))
        if numero ==0:
            sys.exit()
        lado = int(input("Digite la medida del lado:\n"))
        return numero, lado
    def principal(self):
        numero = 4
        while numero !=0:
            numero, lado = self.opciones()
            if numero == 1:
                self.medidas(lado)
            elif numero ==0:
                sys.exit()
            elif numero not in [0,1]:
                sys.exit()
if __name__ == "__main__":
    text = "ingrese la figura su respectivo medicion:\n 1.Rectangulo\n 2. Cilindro\n  3.Triangulo\n 4.Cubo\n 0.Salir\n"
    numero = int(input(text))
    if numero==1: 
        rectangulo = Rectangulo()
        rectangulo.principal()
    elif numero ==2:
        cilindro=Cilindro()
        cilindro.principal()
    elif numero ==3:
        triangulo=Triangulo()
        triangulo.principal()
    elif numero ==4:
        cubo=Cubo()
        cubo.principal()
    elif numero == 0:
        sys.exit()
