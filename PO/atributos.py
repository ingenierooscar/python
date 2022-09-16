#atributos son variables
#hay dos instancia y la de la clase
#los de instancia estan en el init

class Persona:
    variable_de_la_clase = 123

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

paco = Persona("paco", 20)
print(paco.nombre)
print(paco.edad)
print(paco.variable_de_la_clase)