from tkinter import*

ventana = Tk()

ventana.title("Posicionar")
ventana.geometry("400x200")

etiqueta1= Label(ventana, text="Saluda desde aqui")
etiqueta1.place(x=30, y=50)

etiqueta2= Label(ventana, text="Minimizar desde aqui")
etiqueta2.place(x=30, y=100)
def saludo():
    label1= Label(ventana, text="Te saludo")
    label1.pack()
boton1= Button(ventana, text="Haz click aqui para saludar", command=saludo)
boton1.place(x=200, y=50)

boton2= Button(ventana, text="Haz click aqui para minimizar", command=ventana.iconify)
boton2.place(x=200, y=100)

ventana.mainloop()