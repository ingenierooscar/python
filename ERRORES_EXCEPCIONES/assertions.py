#assertions es para validar errores
def calcular_promedio(lista):
    assert len(lista) > 0, "la lista esta vacia"
    return sum(lista) / len(lista)

promedio = calcular_promedio(lista=[2])
print(promedio)
