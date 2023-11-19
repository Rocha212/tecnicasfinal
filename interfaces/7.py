from tkinter import*

ventana= Tk()

ventana.title("Calculadora")
ventana.geometry("300x350")
ventana.resizable(False,False)
contador1=0
contador2=100
def crearboton(x, contador1, contador2):
    
    boton= Button(ventana, text=f"{x}", width=8,height=2)
    boton.place(x=contador1, y=contador2)

    if contador1==300:
        contador2 +=50
        return contador2 
    else:
        contador1 +=75
        return contador1 

num7= crearboton(7,contador1, contador2)
contador1 += num7
num8= crearboton(8,contador1, contador2)
contador1 += num7
num9= crearboton(9,contador1, contador2)








ventana.mainloop()