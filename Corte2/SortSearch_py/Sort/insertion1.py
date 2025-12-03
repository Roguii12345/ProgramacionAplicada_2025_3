def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]        # valor que vamos a insertar
        j = i - 1

        # mover los elementos mayores que key hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insertar la key en el hueco que quedó
        arr[j + 1] = key


def printArray(arr):
    for x in arr:
        print(x, end=" ")
    print()


def main():
    arr = [5, 2, 4, 6, 1]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr)

    insertionSort(arr)

    print("Arreglo ordenado:")
    printArray(arr)


if __name__ == "__main__":
    main()
