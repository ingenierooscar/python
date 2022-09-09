#en el arhcivo main podemos llamar las fucniones de los modulos
from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 5
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)

#otra forma de imprimir sin diccionario es usando una variable
perimetro = perimetro_cuadrado(lado)
print(perimetro)

radio = 5
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print(circulo)

#en el archivo main yo puedo llamar los modulos que creen