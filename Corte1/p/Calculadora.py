class Calculadora:
    def __init__(self):
        pass

    def preguntar_operacion(self):
        print("=== Calculadora Girumen ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Raíz cuadrada")
        print("6. Potencia")
        print("7. Factorial")
        opcion = input("Elige una opción (1-7): ")
        return opcion

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: división por cero"
        return a / b

    def raiz(self, a):
        if a < 0:
            return "Error: no se puede sacar raíz de un número negativo"
        x = a
        for i in range(10):
            x = 0.5 * (x + a / x)
        return x

    def potencia(self, a, b):
        resultado = 1
        if b < 0:
            for i in range(int(-b)):
                resultado *= a
            return 1 / resultado
        else:
            for i in range(int(b)):
                resultado *= a
            return resultado

    def factorial(self, a):
        if a < 0:
            return "Error: factorial de número negativo"
        resultado = 1
        for i in range(1, int(a) + 1):
            resultado *= i
        return resultado