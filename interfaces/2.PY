from tkinter import*
import time
ventana= Tk()

ventana.title("mi primera chamba")
ventana.geometry("500x300")

boton1= Button(ventana, text="minimizar", command=ventana.iconify, bg="red")
boton1.pack(side=LEFT)

def imprimir ():
    label1= Label(ventana, text="Imprimiendo...")
    label1.pack()

boton2 = Button(ventana, text="imprimir", command=imprimir, bg="blue")
boton2.pack(side=RIGHT)







ventana.mainloop()