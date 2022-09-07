#un direccion es llave y valor
"""
lenguaje = {
    "nombre": "oscar",
    "apellido": "rodriguez"
}

for llave in lenguaje:
    print("llave:", llave)
    print("valor", lenguaje[llave])

#usando .keys
for elemento in lenguaje.keys():
    print(elemento)

# usando values
for elementos in lenguaje.values():
    print(elementos)

#usando item
for llave , valor in lenguaje.items():
    print(llave, valor)

#para pasarlo como una tupla
for elemento in lenguaje.items():
    print(elemento)"""

frutas = ["manzana", "naranja", "piña"]
for fruta in frutas:
    
    print("fruta: ", fruta)
    print("tiene: ", len(fruta), " letras")