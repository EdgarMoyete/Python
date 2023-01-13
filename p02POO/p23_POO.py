# Edgar Moises Hernandez Gonzalez
# 21/06/21
# Llamar una clase desde otro archivo

from p23POOimc import Obesidad

personas = {'Edgar': (79, 1.68), 'Moises': (88, 1.68)}

obj_obesidad_1 = Obesidad(personas['Edgar'][0], personas['Edgar'][1])
obj_obesidad_2 = Obesidad(personas['Moises'][0], personas['Moises'][1])
print(obj_obesidad_1.informacion())
print(obj_obesidad_2.informacion())