numeros = input("Ingresa una lista de números: ")

lista_numeros = [int(numero) for numero in numeros.split(",")]

lista_numeros.sort()

print(lista_numeros)

print("Fin.")
