n=int(input("ingrese el numero a mirar la cantidad de digitos: "))

cont=0
num=n
divi=10
cambiazo=-1
if (num<0):
    num= num *cambiazo
else:
    num = num*1

while(num>1):
    num= num/divi

    cont +=1
print("La cantidad de digitos por el numero ingresado es: ",cont)
