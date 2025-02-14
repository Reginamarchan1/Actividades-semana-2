numeros = input("Introduce una lista de números separados por comas: ")

lista_numeros = [int(numero) for numero in numeros.split(",")]

suma = sum(lista_numeros)

print(f"La suma de todos los elementos de la lista es: {suma}")

print("Fin.")