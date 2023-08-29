num= (input("Digite un numero de 5 cifras para sumar sus componentes: "))

sumat=()

for saltador in num:
    sumat= sumat+ (saltador,)


suma=0

for i in range (len(sumat)):
    suma += int(sumat[i])

print("la suma de los componentes del numero son; ", suma)