#las tuplas son inmutables son entre parentesisi ()

lenguajes = ("python", "c", "c++")

lenguajes2 = "go", "java"        #toma por defecto como tupla
print(lenguajes)
print(lenguajes2)

#acceder por medio de indices lenguajes[]
print(lenguajes[1])

#para acceder al ultimo elemento lenguajes[-1]
print(lenguajes[-1])

#son inmutables no se pueden cambiar
lenguajes[0] = "va a fallar"
print(lenguajes)

#menor tiempo de procesamiento y nunca la vas a por cambiar