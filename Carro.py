class Carro():
    def __init__(self, marca, modelo, color, puertas, velocidades):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        self.velocidades = velocidades

    def setMarca(self,marca):
        self.marca = marca

    def setmodelo(self,modelo):
        self.modelo = modelo
    
    def setColor(self,color):
        self.color = color

    def setPuertas(self,puertas):
        self.puertas = puertas
    
    def setVelocidades(self,velocidades):
        self.velocidades = velocidades



    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getColor(self):
        return self.color

    def getPuertas(self):
        return self.puertas
    
    def getVelocidades(self):
        return self.velocidades
