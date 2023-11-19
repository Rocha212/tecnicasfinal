lista=[3,3,8,8,8,1,1,1,2,2,10,10]

grupos=[]

gruposdef=[]
for i in range(len(lista)-1):
    lista2=[]
    if lista[i] == lista[i+1]:

        x=lista.count(lista[i])
        
        for p in range (x):

          lista2.append(lista[i])
    if len(lista2) !=0:
        grupos.append(lista2)
        gruposdef.append(lista2)


for j in range (len(grupos)-1):
    
    if grupos[j]== grupos[j+1]:
    
        del gruposdef[j]

print(f"tiene {len(gruposdef)} grupos y son: " ,gruposdef)




        