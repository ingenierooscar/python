#son los imports o librerias que en python hay
import datetime
time_now = datetime.datetime.now()
print(time_now)

#otra forma de importar es com alias as
import datetime as dt
time_as = dt.datetime.now()
print(time_as)

#otra forma es importando solo el modulo que necesitamos del paquete
from datetime import datetime
time_from = datetime.now()
print(time_from)