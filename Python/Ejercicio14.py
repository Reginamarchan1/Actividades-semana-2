n = int(input("Ingresa la cantidad de números aleatorios que deseas generar: "))

a = 1103515245
c = 12345
m = 2**31

lista = len(str(n))

numeros_aleatorios = []
for _ in range(n):
    
    lista = (a * lista + c) % m
    numero_aleatorio = (lista % 100) + 1
    numeros_aleatorios.append(numero_aleatorio)

print("Lista de números aleatorios generada:", numeros_aleatorios)
