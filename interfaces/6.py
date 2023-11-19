from tkinter import*
from tkinter import messagebox
ventana = Tk()

menubar= Menu(ventana)

ventana.config(menu=menubar)


def cerrar ():
    messagebox.askquestion("Cerrar", message="Estas seguro?")

def licencia():
    messagebox.showinfo("Version", message="Version 1.0")








archivo = Menu(menubar, tearoff=0)
archivo.add_command(label="Nuevo")
archivo.add_command(label="abrir")
archivo.add_command(label="guardar")
archivo.add_command(label="cerrar", command=cerrar)
archivo.add_separator()
archivo.add_command(label="salir", command=ventana.quit)

edit=Menu(menubar, tearoff=0)

edit.add_command(label="cortar")
edit.add_command(label="copiar")
edit.add_command(label="pegar")

ayuda= Menu(menubar,tearoff=0)

ayuda.add_command(label="ayuda", command=licencia)


menubar.add_cascade(label="archivo", menu= archivo)
menubar.add_cascade(label="editar", menu= edit)
menubar.add_cascade(label="ayuda", menu= ayuda)
ventana.mainloop()