numeros = input("Introduce una lista de numeros: ")

lista_numeros = [int(numero) for numero in numeros.split(",")]

mayor = max(lista_numeros)
menor = min(lista_numeros)

print(f"El número mayor es {mayor} y el menor es {menor}")

print("Fin.")
