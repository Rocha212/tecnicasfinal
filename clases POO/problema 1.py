class carro:

    def __init__(self, marca, modelo):

        self.marca= marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, velocidad):

        self.velocidad += velocidad
    
    def frenar (self, velocidad):

        if self.velocidad <= velocidad:

            self.velocidad = 0
        else:

            self.velocidad -= velocidad
    
    def mostrarinfo (self):

        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("velocidad: ", self.velocidad)

carro1 = carro('Toyota', 'Prado')
carro1.mostrarinfo()
carro1.acelerar(50)
carro1.mostrarinfo()
carro1.frenar(10)
carro1.mostrarinfo()
