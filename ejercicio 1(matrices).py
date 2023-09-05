mnula=[[0,0,3,0,0],
       [0,0,0,0,0],
       [0,6,1,0,0],
       [0,0,0,0,0],
       [0,0,0,0,1],]

mcompacta=[]

filacompac=[]

for i in range (len(mnula)):

    for j in range( len(mnula[i])):


        if (mnula[i][j]!=0):
            fila=i+1

            columna=j +1
            valor = mnula[i][j]
            
            mcompacta.append([fila, columna, valor])
            
            
            

print(mcompacta)