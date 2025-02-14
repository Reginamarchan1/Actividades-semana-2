numero = int(input("Introduce un número: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    i = 2
    while i <= int(numero ** 0.5):
        if numero % i == 0:
            es_primo = False
        i += 1

if es_primo:
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")

print("Fin.")
  