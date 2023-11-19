import socket

#configuracion del servidor

host= "localhost"
puerto= 23

servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, puerto))

#Escuchar conexiones entrantes

servidor.listen(1)
print(f"servidor escuchando en: {host}:{puerto} ")

#esperar a que el cliente se conecte 

conexion, direccion= servidor.accept()

#manejar comunicacion con el cliente

while True:

    datos= conexion.recv(1024)
    if not datos:
        break
    
    #convertir los datos recibidos

    msg= datos.decode("utf-8")
    print(f"mensaje recibido: {msg}")

    respuesta = "Mensaje recibido"
    conexion.send(respuesta.encode("utf-8"))
