import socket

#configuracion del cliente para la conexion

host = "localhost"
puerto = 23

#crear un objeto socket para el cliente

cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar el cliente al servidor

cliente.connect((host,puerto))

#enviar datos al servidor

mensaje= "Hola..."

cliente.send(mensaje.encode("utf-8"))

#Recibir la respuesta del servidor
datos_recibidos= cliente.recv(1024)

print(datos_recibidos.decode("utf-8"))

#cerrar la conxexion despues de enviar el mensaje
cliente.close()