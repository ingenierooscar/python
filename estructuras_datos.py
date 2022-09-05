"""las estructuras de datos son:
lista = [elemnto_1, elemento_2]
tupla = (elemnto_1, elemento_2)
diccionario = {llave:valor}
set = {elemento_uco_1, elemento_unico_2}
"""
lenguajes = ["java", "golang", "python"]
programacion = ["lenguajesa", "c++", "c"]       #anidado
lenguajes[0] = "dart"                        #añadir cambiando el elemento en la lista
print(lenguajes)
print(lenguajes[0])
print(len(lenguajes))
print(lenguajes[2])
print(lenguajes[0:2])
print(programacion)
print(programacion[0][0])
print(lenguajes)
lenguajes.append("python")                 #añadir a la lista pero a lo ultimo
print(lenguajes)
lenguajes.extend(programacion)             #une dos listas
print(lenguajes)