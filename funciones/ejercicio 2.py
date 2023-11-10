def es_par(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return es_par(n - 2)

numero = int(input("Introduce un número entero: "))

if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")


