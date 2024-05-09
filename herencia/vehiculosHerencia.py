class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo

class Avion(Vehiculo):
    def __init__(self, color, ruedas, **impulso):
        super().__init__(color, ruedas)
        self.impulso = impulso

    def mostrar_detalle(self):
        print(f'Avion: {self.color} {self.ruedas} {self.impulso}')

vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

coche = Coche('Azul', 4, 150)
print(coche)

bicicleta = Bicicleta('Blanca', 2, 'Urbano')
print(bicicleta)

avion = Avion('Gris', 6, turbo_motores =2)
avion.mostrar_detalle()