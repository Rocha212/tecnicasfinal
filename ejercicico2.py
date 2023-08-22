n=int(input("Ingrese la cantidad de alturas a promediar: "))
div=n
num = 0

while(n>0):
    alt= float(input("Ingrese la altura (Metros)"))
    
    num +=alt

    n -=1

prom= num/div

print("el promedio de las alturas totales son: ", prom)