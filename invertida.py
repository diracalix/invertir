
def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

cadena_usuario = input("Ingrese una cadena de caracteres: ")

cadena_invertida = invertir_cadena(cadena_usuario)

print("Cadena invertida:", cadena_invertida)
