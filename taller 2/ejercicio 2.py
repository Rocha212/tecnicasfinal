def potencia(x,y):

    if y==0:

        return 1
    
    elif y ==1:
        return x
    

    else:

        valor = x* potencia(x,y-1)

        return valor
    
n= potencia(2,5)

print (n)
        