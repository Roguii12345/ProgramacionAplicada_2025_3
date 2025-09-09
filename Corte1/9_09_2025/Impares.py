#Es ejercicio vale una decima del semestre
import os

try:
    while True:
        # pedir número al usuario
        num = input("Ingresa un número: ")
        
        # limpiar consola
        os.system("cls" if os.name == "nt" else "clear")
        
        # convertir a entero
        try:
            num = int(float(num))  # acepta enteros o decimales
        except ValueError:
            print("Entrada inválida, escribe un número.")
            continue
        
        # recorrer del 1 hasta num
        for i in range(1, num+1):
            if i % 2 == 0:
                print(f"{i} es par")
            else:
                print(f"{i} es impar")

except KeyboardInterrupt:
    print("\nPrograma detenido por el usuario.")