numero = input("Ingresa un numero entero: ")

suma_digitos = 0

for digito in numero:
    suma_digitos += int(digito)

print("La suma de los digitos es: ", suma_digitos)

print("Fin.")