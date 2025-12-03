# Busca la primera aparición de key en arr.
# Si la encuentra, devuelve el índice (0, 1, 2, ...)
# Si NO la encuentra, devuelve -1.
def linearSearch(arr, key):
    for i in range(len(arr)):      # recorro el arreglo desde 0 hasta n-1
        if arr[i] == key:          # comparo el elemento actual con key
            return i               # lo encontré, retorno la posición
    return -1                      # no lo encontré en ninguna posición


# Busca TODAS las apariciones de key en arr.
# Devuelve una lista con todos los índices donde aparece key.
def linearSearchAll(arr, key):
    indices = []                  # lista vacía para guardar posiciones
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)     # guardo el índice donde lo encontré
    return indices                # retorno todas las posiciones encontradas


def main():
    # Arreglo de ejemplo
    arr = [4, 9, 2, 7, 5, 7, 9, 7]
    n = len(arr)

    print("Arreglo:", arr)

    key = int(input("Ingrese el número a buscar: "))

    # --- Búsqueda de una sola posición (primera aparición) ---
    pos = linearSearch(arr, key)

    if pos == -1:
        print(f"El número {key} NO se encuentra en el arreglo.")
    else:
        print(f"El número {key} se encuentra (al menos) en la posición {pos} (índice 0-based).")

    # --- Búsqueda de todas las posiciones donde aparece key ---
    indices = linearSearchAll(arr, key)
    count = len(indices)

    if count == 0:
        print(f"No se encontraron ocurrencias de {key}.")
    else:
        print(f"El número {key} aparece {count} veces, en las posiciones:", indices)


if __name__ == "__main__":
    main()
