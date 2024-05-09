class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Alejandro', 'Arelis', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()

persona2 = Persona('Hanna', 'Arelis', 0)
persona2.mostrar_detalle()

persona3 = Persona('Juan', 'Perez', 28, '123',123, ejemplo='juanito perez')
persona3.mostrar_detalle()

persona3.nombre = 'Juan Carlos'
persona3.apellido = 'Juarez'
persona3.edad = 25
persona3.mostrar_detalle()

persona4 = Persona('Karla', 'Gomez', 30)
persona4.terminos = {
    'valor1':'valor 1'
}
persona4.mostrar_detalle()

nombre = str(input('Proporciona el nombre: '))
apellido = str(input('Proporciona el apellido: '))
edad = int(input('Proporciona la edad: '))

persona5 = Persona(nombre, apellido, edad)
persona5.mostrar_detalle()