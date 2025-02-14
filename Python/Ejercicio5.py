cadena = input("Introduce una cadena: ")

vocales = "aeiouAEIOU"

vocales_en_cadena = [letra for letra in cadena if letra in vocales]

print("Las vocales encontradas en la cadena son: ", vocales_en_cadena)

print("Fin.")
