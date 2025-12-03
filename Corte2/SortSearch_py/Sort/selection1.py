def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIndex = i  # asumimos que el menor está en i

        # buscar el menor en el resto del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # si encontramos un menor, intercambiamos
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]


def printArray(arr):
    for num in arr:
        print(num, end=" ")
    print()


# Programa principal
arr = [5, 3, 6, 1, 4]

print("Arreglo original:")
printArray(arr)

selectionSort(arr)

print("Arreglo ordenado:")
printArray(arr)
