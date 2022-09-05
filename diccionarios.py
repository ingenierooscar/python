#Json es un diccionario, se usan llaves son un tipo de estructuras de datos que usan llave y valor
#los diccionarios contienen llavar y valor (key and values) son unico

lenguaje = {"nombre" : "python", "creador" : "Guido"}
print(lenguaje)

#añadir key and value
lenguaje["año"] = 1999
print(lenguaje)

#añadir nuevo elemento ya sean otro diccionario o tupla
lenguaje["caracteristicas"] = ["sencillo", "facil", "genial"]
print(lenguaje)

# se pueden consultar por medio de tupla item, keys and values
print(lenguaje.items())
print(lenguaje.keys())
print(lenguaje.values())
