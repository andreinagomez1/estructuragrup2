def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def encontrar_mayor_menor_intermedio():
    primos = []
    while len(primos) < 5:
        try:
            num = int(input("Ingrese un número primo: "))
            if es_primo(num):
                primos.append(num)
            else:
                print("El número no es primo. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    primos.sort()
    mayor = primos[-1]
    menor = primos[0]
    intermedio = primos[2]

    print("Número mayor:", mayor)
    print("Número menor:", menor)
    print("Número intermedio:", intermedio)
encontrar_mayor_menor_intermedio()
