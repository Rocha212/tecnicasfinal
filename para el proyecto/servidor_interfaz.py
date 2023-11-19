from tkinter import*
import socket
import threading

ventana= Tk()

ventana.geometry("450x500")
ventana.resizable(0,0)
ventana.title("Interfaz Servidor")
ventana.configure(bg="dark gray")

host="127.0.0.1"
puerto1=IntVar()
envio= StringVar()

def conectar():
    puerto=puerto1.get()
    
    servidor.bind((host,puerto))
    servidor.listen(1)
    hilo_conexion = threading.Thread(target=manejar_conexion)
    hilo_conexion.daemon = True
    hilo_conexion.start()


def manejar_conexion():
    global conexion
    while True:
        conexion, direccion = servidor.accept()
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo_cliente.daemon = True
        hilo_cliente.start()

def manejar_cliente(conexion, direccion):
    while True:
        data = conexion.recv(1024)
        if not data:
            break
        mensaje = data.decode("utf-8")
        numlineas= recibidos.get("1.0", END).count("\n")
        if numlineas>lineasRecibidos:
            recibidos.delete("1.0", f"{numlineas - lineasRecibidos + 1}.0")
        recibidos.insert(END, mensaje + "\n")

def enviarmsg():

    numlineas= enviados.get("1.0", END).count("\n")
    if numlineas>lineasEnviados:
        enviados.delete("1.0", f"{numlineas - lineasEnviados + 1}.0")
    frase=envio.get()
    enviados.insert(END,frase + "\n")
    frase2= frase.encode("utf-8")
    conexion.send(frase2)


etiqueta1= Label(ventana, text="Chat 1.0", bg="gray", bd=10, width=60,font="consola 20")
etiqueta1.pack()

etiqueta2= Label(ventana, text="Conectarse para chatear", bg="light green", bd=5, font="consola 8" )
etiqueta2.place(x=90, y=57)

etiqueta4= Label(ventana, text="Puerto", bg="dark gray",bd=5, font="consola 7", width=8)
etiqueta4.place(x=50, y=90)

etiqueta5= Label(ventana, text="Desconectarse del Chat", bg="red", bd=5, font="consola 8" )
etiqueta5.place(x=270, y=57)

etiqueta6= Label(ventana, text="Mensajes Recibidos:", font="consola 12", width=20, bg="gray")
etiqueta6.place(x=20, y=130)

etiqueta7= Label(ventana, text="Mensajes Enviados:", font="consola 12", width=20, bg="gray")
etiqueta7.place(x=20, y=300)

etiqueta8= Label(ventana, text="Enviar mensaje:", font="consola 12", width=17, height=2)
etiqueta8.place(x=20, y=450)

boton1= Button(ventana, text="Conectar", bd=3, bg="light green", command=conectar)
boton1.place(x=180, y=87)

boton2= Button(ventana, text="Desconectar", bd=3, bg="red", command=ventana.quit)
boton2.place(x=295, y=87)

boton3= Button(ventana, text="Enviar", bd=10, bg="light gray", command=enviarmsg)
boton3.place(x=380, y=450)

entrada2=Entry(ventana, bd= 3, bg="gray",width=5, textvariable=puerto1)
entrada2.place(x=100, y=90)

entrada3= Entry(ventana, bd=13, width=25, textvariable=envio)
entrada3.place(x=190, y=450)

recibidos=Text(ventana, height=8, width=52, state=NORMAL)
recibidos.place(x=20,y=160)
lineasRecibidos=8

enviados=Text(ventana, height=7, width=52, state=NORMAL)
enviados.place(x=20,y=328)
lineasEnviados=7


servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ventana.mainloop()