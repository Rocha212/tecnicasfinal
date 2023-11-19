a=[]

n=int(input("ingrese el numero de valores para que poner en la lista: "))

for q in range (n):

    p= int(input(f"ingrese el numero {q+1}: "))

    a.append(p)
suma=0

for i in range (len(a)-1):

    resta = a[i+1]- a[i]

    suma += resta


print (suma)