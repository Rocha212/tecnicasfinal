from tkinter import*

ventana = Tk()

ventana.title("entrada")
ventana.geometry("300x300")

nombre=StringVar()
apellido=StringVar()
saludo=StringVar()


def saludar():
    saludo.set(f"Hola {nombre.get()} {apellido.get()}")





etiqueta1= Label(ventana, text="Escribe aqui tu nombre: ", bd=4, bg="gray",font=("Curier 10 "))
etiqueta1.place(x=10,y=10)
entrada1=Entry(ventana,textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)

etiqueta2= Label(ventana, text="Escribe aqui tu apellido: ", bd=4, bg="gray",font=("Curier 10 "))
etiqueta2.place(x=10,y=40)
entrada2=Entry(ventana,textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)

boton1= Button(ventana, text="Saludar", command=saludar,bd=5,bg="gray")
boton1.place(x=125,y=100)

entrada3=Entry(ventana, bd=20, font=("Curier 10"), textvariable=saludo, state="disabled")
entrada3.place(x=70, y=200)



ventana.mainloop()