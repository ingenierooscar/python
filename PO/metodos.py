class Persona:

    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

    def cumplir_años(self):
        self.edad += 1
        print(f"Feliz cumple {self.edad} {self.nombre}")

paco = Persona(edad=20, nombre = "paco")
paco.cumplir_años()

#herencia
class Empleado(Persona):
    def __init__(self, edad, nombre, horas_totales):  #sin esto daria error porqueno compartiria las variables de la clase persona
        super(Empleado, self).__init__(edad, nombre)
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"usted ha trabajado {horas_trabajadas} horas")
        print(f"horas totales: {self.horas_totales}")

paco = Empleado(nombre="paco", edad=20, horas_totales=8)
paco.trabajar(horas_trabajadas=2)
paco.cumplir_años()