def contar_vocales_modificar_frase():
    frase = input("Ingrese una frase: ")
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for letra in frase if letra in vocales)
    frase_modificada = ''.join(letra.upper() if letra in vocales else letra.lower() for letra in frase)

    print(f"La frase cuenta con {cantidad_vocales} vocales.")
    print("Frase modificada:", frase_modificada)

contar_vocales_modificar_frase()
