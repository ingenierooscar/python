from ast import If
from contextlib import nullcontext
from operator import truediv
from queue import Empty
import string


a = 4
b = 2
c = True

"""if a < b:
    print("A es menos")
elif a == b:
    print("son iguales")    
else:
    print("A es mayor") 
"""

if c:
    print("c es verdadero")
else:
    print("c es falso")

if type(c) is bool:
    print("is bollena")
else:
    print("no lo es")       

if type(a) is int and a > b:
    print("a es un numero")
else:
    print("no lo es")