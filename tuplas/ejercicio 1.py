n=(input("diga una palabra o frase que se quiera contar laas vocales: "))

frase = n

vocales= "a", "e", "i", "o", "u"

contador=0

for saltador in frase:

    if saltador in vocales:
        contador +=1

print("La cantidad de vocales de su palabra o frase son: ", contador)


