from unittest import result


def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def area_cuadrada(lado):
    area = lado * lado
    return area         # si se le quita el retorno dara error None

perimetro = perimetro_cuadrado(lado=5)
area =  area_cuadrada(lado=5)

print(f"area: {area}, perimetro {perimetro}")

#tambien devuelve tuplas o usando dos variables 
def calcular_perimetro(lado):
    perimetros = lado * 4
    areas = lado * lado
    return areas, perimetros

resultado = calcular_perimetro(lado=2)
print(resultado)
#print(f"area: {areas}, Perimetro: {perimetros}")