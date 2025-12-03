def merge(arr, l, m, r):
    n1 = m - l + 1       # tamaño del subarreglo izquierdo
    n2 = r - m           # tamaño del subarreglo derecho

    # subarreglos temporales
    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    i = 0  # índice en L
    j = 0  # índice en R
    k = l  # índice en arr

    # mezclar L[] y R[] dentro de arr[l..r]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copiar lo que quede de L
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copiar lo que quede de R
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # ordenar primera mitad y segunda mitad
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # mezclar ambas
        merge(arr, l, m, r)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    mergeSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    for x in
