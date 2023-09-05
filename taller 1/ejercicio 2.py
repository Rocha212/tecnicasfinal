a=int(input("ingrese un numero: "))
b= int(input("ingrese otro numero: "))

num=0

if a==b:
    print("El mcd de los 2 numeros es: ", a)

elif a>b:
    while b%a!=0:
        num=a
        a=b%a
        b=num
    print("el mcd de los 2 numeros es: ", a)
else:
    while a%b!=0:
        num=b
        b=a%b
        a=num
    print("el mcd de los 2 numeros es: ", b)