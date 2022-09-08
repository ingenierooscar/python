# en python se puede documentar y se usa docs string, se hace de forma corta y larga

def perimetro_cuadradro(lado):
    """calcular el perimetro de un cuadrado
    
    esta funcion recibe el valor de un lado del cuadrado y retorna el calculo

    Args:
    lado (int): medidas de los lados

    Returns:
    perimetro (int): perimetro del cuadrado
    """
    perimetro = lado * 4
    return perimetro

perimetro_cuadradro(lado=5)