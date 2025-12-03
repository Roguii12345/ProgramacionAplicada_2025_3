def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):                     # FOR EXTERNO
        for j in range(n - i - 1):             # FOR INTERNO
            if arr[j] > arr[j + 1]:            # CONDICIÓN DE INTERCAMBIO
                # INTERCAMBIO
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def printArray(arr):
    for x in arr:
        print(x, end=" ")
    print()


def main():
    arr = [5, 1, 4, 2, 8]
    n = len(arr)

    print(f"Tamaño del arreglo: {n}")

    print("Arreglo original:")
    printArray(arr)

    bubbleSort(arr)

    print("Arreglo ordenado:")
    printArray(arr)


if __name__ == "__main__":
    main()
