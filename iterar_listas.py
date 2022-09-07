#iterar con for normal
lenguajes =["python", "java", "c#"]
for elemento in lenguajes:
    print(elemento)

#usando range con for
for index in range(len(lenguajes)):
    print("indice", index)
    print("elemento", lenguajes[index])

#usando while
i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1
