n= int(input("Diga la cantidad de precios a listar: "))


precios=()


for i in range(n):

    v=int(input(f"diga el precio numero {i+1}, para listar: "))

    precios= precios + (v,)


print("El precio minimo de la lista de precios es: ", min(precios), " y el precio maximo es: ", max(precios))