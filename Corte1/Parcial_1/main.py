from Calculadora import Calculadora
from Areas import Areas

class Main:
    @staticmethod
    def ejecutar():
        while True:
            try:
                print("\n==============================")
                print("      MENÚ PRINCIPAL ")
                print("==============================")
                print("1. Calculadora")
                print("2. Áreas")
                print("==============================")
                opcion = input("Elige una opción (1 o 2): ")

                if opcion == "1":
                    calc = Calculadora()
                    op = calc.preguntar_operacion()

                    if op in ["1", "2", "3", "4", "6"]:
                        a = float(input("Ingrese el primer número: "))
                        b = float(input("Ingrese el segundo número: "))
                    elif op in ["5", "7"]:
                        a = float(input("Ingrese el número: "))
                    else:
                        print("Opción no válida.")
                        continue

                    print("\n--- Resultado ---")
                    if op == "1":
                        print(calc.suma(a, b))
                    elif op == "2":
                        print(calc.resta(a, b))
                    elif op == "3":
                        print(calc.multiplicacion(a, b))
                    elif op == "4":
                        print(calc.division(a, b))
                    elif op == "5":
                        print(calc.raiz(a))
                    elif op == "6":
                        print(calc.potencia(a, b))
                    elif op == "7":
                        print(calc.factorial(a))
                    else:
                        print("Opción no válida.")

                elif opcion == "2":
                    area = Areas()
                    op = area.preguntar_area()

                    if op == "1":
                        lado = float(input("Ingrese el lado del cuadrado: "))
                        print("Área:", area.cuadrado(lado))
                    elif op == "2":
                        base = float(input("Ingrese la base del rectángulo: "))
                        altura = float(input("Ingrese la altura del rectángulo: "))
                        print("Área:", area.rectangulo(base, altura))
                    elif op == "3":
                        radio = float(input("Ingrese el radio de la circunferencia: "))
                        print("Área:", area.circunferencia(radio))
                    elif op == "4":
                        base = float(input("Ingrese la base del triángulo: "))
                        altura = float(input("Ingrese la altura del triángulo: "))
                        print("Área:", area.triangulo_rectangulo(base, altura))
                    else:
                        print("Opción no válida.")
                else:
                    print("Opción no válida.")

            except KeyboardInterrupt:
                print("\n\n👋 Programa finalizado por el usuario.")
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    Main.ejecutar()