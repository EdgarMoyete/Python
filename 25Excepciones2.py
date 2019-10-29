#Edgar Moises Hernandez-Gonzalez
#03/01/19-08/01/19
#Excepciones 2

import math

try:
	a = int(input("Ingrese a: "))
	b = int(input("Ingrese b: "))
	c = int(input("Ingrese c: "))
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	print("X1:", x1, "\nX2:", x2)
except:
	print("ERROR")
finally:
	print("Esto siempre se ejecuta")