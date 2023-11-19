#n=int(input("ingrese el tamaño de la matriz"))

m=4

matriz=[]

fila=[]

for i in range(m):

    

    fila.append(0)
    
    matriz.append(fila)

for p in range(len(matriz)):

    for j in range (len(matriz[p])):

        if p==j:
            matriz[p][j]=1
        break
            


print(matriz)