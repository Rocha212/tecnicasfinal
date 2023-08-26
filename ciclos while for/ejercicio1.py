n=int(input("ingrese el numero de estudiantes: "))

ap=0
rep=0

while n>0:
    nota=float(input("Ingrese la nota del estudiante: "))
    if (nota >=3):
        ap +=1
        n -=1
    else:
        rep +=1
        n -=1

print("Los que aprueban son: ",ap, " y los que reprueban son: ", rep)