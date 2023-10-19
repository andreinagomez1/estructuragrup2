def extraer_caracteres_entre_indices():
    frase = input("Ingrese una frase: ")
    try:
        inicio = int(input("Ingrese el índice de inicio: "))
        fin = int(input("Ingrese el índice de fin: "))
        resultado = frase[inicio:fin]
        print("Caracteres entre los índices:", resultado)
    except ValueError:
        print("Por favor, ingrese índices válidos.")

extraer_caracteres_entre_indices()
