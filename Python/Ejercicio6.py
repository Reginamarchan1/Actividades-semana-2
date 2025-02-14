num = int(input("Ingresa un numero: "))

print(f"La tabla de multiplicar de {num} es: ")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

print("Fin.")