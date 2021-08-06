# clase contacto
class Contacto:
    def __init__(self, nombre, telefono, edad):
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad

    def muestraDetalles(self):
        print("Nombre: {} Numero de telefono: {} Edad: {}".format(self.nombre, self.telefono, self.edad))

    def actualizacion_contacto(self, nombre, telefono, edad):
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        print("Actualización correcta")

