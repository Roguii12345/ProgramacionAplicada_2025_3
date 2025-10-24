class Areas:
    def __init__(self):
        pass

    def preguntar_area(self):
        print("=== Cálculo de Áreas ===")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Circunferencia")
        print("4. Triángulo rectángulo")
        opcion = input("Elige una opción (1-4): ")
        return opcion

    def cuadrado(self, lado):
        return lado * lado

    def rectangulo(self, base, altura):
        return base * altura

    def circunferencia(self, radio):
        pi = 3.1416 
        return pi * radio * radio

    def triangulo_rectangulo(self, base, altura):
        return (base * altura) / 2
