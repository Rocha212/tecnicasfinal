caracter= input("ingrese un caracter para comprobar que es: ")

vocales= "a", "i", "e", "o", "u"

numeros= "0","1" ,"2" , "3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"

if caracter in vocales:
    print(f"su caracter:  ({caracter}) es una vocal")

elif caracter in numeros:
    print(f"su caracter:  ({caracter}) es un numero")

else:
    print(f"su caracter:  ({caracter}) es una consonante")