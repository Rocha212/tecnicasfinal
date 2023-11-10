listaEstudiantes = []

calificaciones=[]

n= int(input("cantidad de estudiantes a poner calificaciones: "))

for i in range (n):

    m= input(f"ingrese el nombre del estudiante #{i+1}: ")
    listaEstudiantes.append(m)

x = int(input("cantidad de calificaciones a poner: "))
for j in range (len(listaEstudiantes)):

    calificacion = []
    
    promedio=0
    for k in range (x):

        y= float(input(f"cual es la calificacion definitiva de la asignatura#{k+1} del estudiante {listaEstudiantes[j]}: "))

        calificacion.append(y)
        promedio +=y
    
    calificacion.append(promedio/x)
    calificaciones.append(calificacion)

print(listaEstudiantes)

print(calificaciones)