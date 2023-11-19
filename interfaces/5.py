from tkinter import*

ventana = Tk()

ventana.title("Radiobuttons")
ventana.geometry("400x300")
ventana.resizable(False,False)
ventana.config(bg="gray")

opcion=IntVar()
num= IntVar()

def operacion ():

    numero=num.get()

    if opcion.get()==1:
        total= numero*5
    elif opcion.get()==2:
        total= numero*10
    elif opcion.get()==3:
        total= numero*20
    elif opcion.get()==4:
        total= numero*30
    elif opcion.get()==5:
        total= numero*40
    else:
        total = numero* numero

    print(f"el numero total de la operacion es: {str(total)}")

 




etiqueta1=Label(ventana, text="Escriba su numero: ", bd=5, bg="gray")
etiqueta1.place(x=20, y=20)

entrada1=Entry(ventana,textvariable=num, bd=5, bg="gray")
entrada1.place(x=150,y=20)

etiqueta2=Label(ventana, text="Elija la cantidad: ", bd=5, bg="gray")
etiqueta2.place(x=120, y=50)

x5= Radiobutton(ventana, text="x5", value=1, bd=5, bg="gray", variable=opcion)
x5.place(x=30, y=80)

x10= Radiobutton(ventana, text="x10", value=2, bd=5, bg="gray", variable=opcion)
x10.place(x=80, y=80)

x20= Radiobutton(ventana, text="x20", value=3, bd=5, bg="gray", variable=opcion)
x20.place(x=130, y=80)

x30= Radiobutton(ventana, text="x30", value=4, bd=5, bg="gray", variable=opcion)
x30.place(x=180, y=80)

x40= Radiobutton(ventana, text="x40", value=5, bd=5, bg="gray", variable=opcion)
x40.place(x=230, y=80)

boton1=Button(ventana, text="Realizar operacion", bd=5, bg="gray", command=operacion)
boton1.place(x=120, y=120)










ventana.mainloop()
