from tkinter import*

ventana = Tk()

ventana.geometry("400x300")

w= Spinbox(ventana, values=("python", "HTML5", "css"))
w.pack()

e= Spinbox(ventana, values=("papa", "puticas", "perras"))
e.pack()

ventana.mainloop()

