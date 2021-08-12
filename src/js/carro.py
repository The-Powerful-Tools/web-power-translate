class Coche:
    def __init__(self,color,placa,modelo,anio):
        self.color = color
        self.placa = placa
        self.modelo = modelo
        self.anio = anio

instancia = Coche("Rojo","234-543-556","Kia K5","2017")

print('Carro\nColor: %s\nPlaca: %s\nModelo: %s\nAño: %s' % (instancia.color,instancia.placa,instancia.modelo,instancia.anio))