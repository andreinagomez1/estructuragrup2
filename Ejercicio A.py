def eliminar_repetidos_y_sumar():
    numeros = []
    while True:
        try:
            num = int(input("Ingrese un número: "))
            if num == 0:
                break
            numeros.append(num)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    numeros_sin_repetir = list(set(numeros))
    suma = sum(numeros_sin_repetir)

    print("Lista sin elementos repetidos:", numeros_sin_repetir)
    print("Suma de los elementos únicos:", suma)

eliminar_repetidos_y_sumar()
