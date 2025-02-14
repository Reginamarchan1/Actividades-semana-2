num = int(input("Ingresa un número entre 1 y 20: "))

if num < 1 or num > 20:
    print("El número debe estar entre 1 y 20")
else:
    factorial = 1
    contador = 1

    while contador <= num:
        factorial *= contador
        contador += 1
    print(f"El número de {num} es:{factorial}")

print("Fin")            