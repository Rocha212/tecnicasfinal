n= int(input("ingrese un número: "))
suma=2

while(n>2):
    if (n%2!=0):
        n -=1
    else:
        suma +=n
        n -=1

print("La suma comprendida entre 2 y el numero dado es: ", suma)