#se usan para recorrer por lo general strings o estructuras de datos

for letras in "hola mundo":
    print(letras)

#una lista 
lenguajes = ["python", "java", "C#"]
for element in lenguajes:
    print(element)

#usando break se detiene en el primer ciclo del for
for letra in "es un texto largo":
    print(letra)
    break

#tambien se puede usar un if para iniciar el break
for elementos in lenguajes:
    print(elementos)
    if elementos == "java":
        break

#Continue es una instruccion para saltar una linea
for elem in lenguajes:
    if elem == "java":
        continue
    print(elem)

#range es una intruccion que inicia de 0 hasta donde le digamos o un intervalo
for num in range(2, 5):
    print(num)

