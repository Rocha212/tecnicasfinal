from tkinter import*

ventana= Tk()

ventana.geometry("450x500")
ventana.resizable(0,0)
ventana.title("Interfaz Cliente")
ventana.configure(bg="dark gray")

numeroip=StringVar()
puerto= IntVar()
envio=StringVar()

def enviarmsg():
    numlineas= enviados.get("1.0", END).count("\n")
    if numlineas>maxlineasEnviados:
        enviados.delete("1.0", f"{numlineas - maxlineasEnviados + 1}.0")
    frase=envio.get()
    enviados.insert(END,frase + "\n")

   

etiqueta1= Label(ventana, text="Chat 1.0", bg="gray", bd=10, width=60,font="consola 20")
etiqueta1.pack()

etiqueta2= Label(ventana, text="Conectarse para chatear", bg="light green", bd=5, font="consola 8" )
etiqueta2.place(x=90, y=60)

etiqueta3= Label(ventana, text="Conexion IP", bg="dark gray",bd=5, font="consola 7")
etiqueta3.place(x=10, y=90)

etiqueta4= Label(ventana, text="Puerto", bg="dark gray",bd=5, font="consola 7", width=8)
etiqueta4.place(x=155, y=90)

etiqueta5= Label(ventana, text="Desconectarse del Chat", bg="red", bd=5, font="consola 8" )
etiqueta5.place(x=315, y=57)

etiqueta6= Label(ventana, text="Mensajes Recibidos:", font="consola 12", width=20, bg="gray")
etiqueta6.place(x=20, y=130)

etiqueta7= Label(ventana, text="Mensajes Enviados:", font="consola 12", width=20, bg="gray")
etiqueta7.place(x=20, y=300)

etiqueta8= Label(ventana, text="Enviar mensaje:", font="consola 12", width=17, height=2)
etiqueta8.place(x=20, y=450)

boton1= Button(ventana, text="Conectar", bd=3, bg="light green")
boton1.place(x=242, y=87)

boton2= Button(ventana, text="Desconectar", bd=3, bg="red", command=ventana.quit)
boton2.place(x=340, y=87)

boton3= Button(ventana, text="Enviar", bd=10, bg="light gray", command=enviarmsg)
boton3.place(x=380, y=450)

entrada1=Entry(ventana, textvariable=numeroip,bd= 3, bg="gray",width=15)
entrada1.place(x=70, y=90)

entrada2=Entry(ventana, bd= 3, bg="gray",width=5)
entrada2.place(x=200, y=90)

entrada3= Entry(ventana, bd=13, width=25,textvariable=envio)
entrada3.place(x=190, y=450)
maxlineasRecibidos=8

recibidos=Text(ventana, height=8, width=52, state=NORMAL)
recibidos.place(x=20,y=160)

enviados=Text(ventana, height=7, width=52, state=NORMAL)
enviados.place(x=20,y=328)
maxlineasEnviados=7












ventana.mainloop()