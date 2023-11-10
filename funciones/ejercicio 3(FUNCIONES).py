def fibonacci(n):

    if n <= 0:
        return []

    elif n ==1:
        return [0]

    elif n == 2:

        return [0,1]

    else:

        lista = fibonacci (n-1)

        lista.append(lista[-1]+lista[-2])
        return lista
    
n= int(input("ingrese el numero hasta que va la serie de fibonacci: "))

print(fibonacci(n))