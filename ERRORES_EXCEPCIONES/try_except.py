#se usa para crear menajes de error

def calcular_promedio(lista):
    assert len(lista) > 0, "la lista esta vacia"
    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio(lista=["hola"])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("la funcion no calculo promedio")
    print(e)