#los parametros son los valores que una funcion puede recibir

def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f"el perimetro es {perimetro} {unidades}")

perimetro_cuadrado(5, "metros")
perimetro_cuadrado(lado=25, unidades= "centimetros")

#se pueden escuchar como argumento o parametro, el argumento es el valor