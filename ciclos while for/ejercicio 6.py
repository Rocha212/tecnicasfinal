n = int(input("ingrese un numero de alturas a promediar: "))

suma=0

for i in range(0,n2,1):
    alt=float(input("ingrese una altura en metros, para promediar: "))

    suma = suma + alt

promedio= suma/n

print("el promedio de todas las alturas digitadas es: ", promedio)