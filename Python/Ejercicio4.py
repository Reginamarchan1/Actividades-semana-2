n = int(input("Ingresa un número entre 1 y 50: "))

if n < 1 or n > 50:
    print("El número debe estar entre 1 y 50")
else:
    a, b = 0, 1

    if n >= 1:
        print(a, end= " ")
    if n >= 2:
        print(b, end= " ")
    for _ in range(3, n+1):
        a,b = b, a+b
        print(b, end= " ")
    print()

print("Fin.")