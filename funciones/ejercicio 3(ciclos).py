n= int(input("ingrese el numero hasta que va la serie de fibonacci: "))

a0=0
a1=1
lista=[a0,a1]
for i in range (n-2):

    
    lista.append(lista[-1]+ lista[-2])

print (lista)