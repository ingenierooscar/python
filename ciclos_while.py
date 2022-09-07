# el ciclo while ejecuta nstrucciones mientras se cumple la condicion
#por lo general usa un contador

i = 1 # contador
while i < 5:
    print(i)
    i += 1

# tambien se puede usar el break con una condicion osea if
i = 1
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break