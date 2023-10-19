class BurbujaSort:
    @staticmethod
    def ordenar(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

arreglo = [4, 6, 9, 88, 45, 52, 15, 65, 78]
BurbujaSort.ordenar(arreglo)
print("Arreglo ordenado:", arreglo)
