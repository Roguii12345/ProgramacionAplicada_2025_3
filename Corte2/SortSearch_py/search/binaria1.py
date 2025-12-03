# Búsqueda binaria modificada para encontrar
# la PRIMERA aparición de key en un arreglo ORDENADO.
# Si la encuentra, devuelve el índice de la primera aparición.
# Si NO la encuentra, devuelve -1.
def firstOccurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid        # Se encontró una ocurrencia
            high = mid - 1      # Seguir buscando a la IZQUIERDA
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


# Búsqueda binaria modificada para encontrar
# la ÚLTIMA aparición de key en un arreglo ORDENADO.
# Si la encuentra, devuelve el índice de la última aparición.
# Si NO la encuentra, devuelve -1.
def lastOccurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid        # Se encontró una ocurrencia
            low = mid + 1       # Seguir buscando a la DERECHA
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


# Programa principal
def main():
    # Arreglo ORDENADO
    arr = [3, 5, 7, 9, 11, 11, 11, 11, 13, 15]

    print("Arreglo (ordenado):", arr)

    key = int(input("Ingrese el número a buscar: "))

    first = firstOccurrence(arr, key)
    last  = lastOccurrence(arr, key)

    if first == -1:
        print(f"El número {key} NO se encuentra en el arreglo.")
    else:
        count = last - first + 1
        print(f"El número {key} aparece {count} veces.")
        print("Posiciones (índices 0-based):", list(range(first, last + 1)))


if __name__ == "__main__":
    main()
