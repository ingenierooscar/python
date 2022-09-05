#estuctura de datos con unicos elementos son llave y se separan por comas

st1 = {1, 2, 3}

#da error porque tiene un unico elemento no son estructuras ordenadas
#set1[0]

#solo puede tener un unico elemento
set2 = {1,1,1,2,2,13,1,4,5,6}
print(set2)

#los sets son mutables pero no puede cambiar sus valores y pueden tener varios tipos de datos
set3 = {"text", 1, 2.0}
print(set3)

#para alterar los sets
st1.add(4)
print(st1)

set2.update([7,8,9])
print(set2)

print(len(set2)) #len contar la longitud

st1.discard(2)
print(st1)

st1.remove(1)
print(st1)

st1.clear()
print(st1)