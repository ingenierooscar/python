#es para que retorne un error de excepcion usando raise exception

def validar(x):
    if x < 1:
        raise Exception("el numero debe ser mayor a 1")
    else:
        print("es mayor a 1")

x = 3
validar(x)