import socket

#datos del equipo servidor

host= "localhost"
puerto= 23

#crear socket para el cliente

cliente= socket.socket()

#nos conectamos a la aplicacion del servidor

cliente.connect((host, puerto))
print(f"conectado al servidor {host} {puerto}")

while True:

    data= input("digite cualquier dato")
    datos= data.encode("utf-8")
    cliente.send(datos)

    data= cliente.recv(1024)
    datos= data.decode("utf-8")

    print(f"la respuesta del servidor es: {datos}")