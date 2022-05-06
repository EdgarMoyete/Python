# Edgar Moises Hernandez-Gonzalez
# 26/10/18-21/06/21
# Generadores

def generarPares(n):
	i = 0
	while i < n:
		yield i * 2
		i += 1

devuelve = generarPares(10)
print(next(devuelve))
print("Puede haber mas codigo")
print(next(devuelve))
for i in range(10):
	print("Hola", i)
print(next(devuelve))
print("Mas codigo =)")
print(next(devuelve))

def devuelve_ciudades(*ciudades):
	for item in ciudades:
		yield from item # te ahorras un for anidado

ciudades = devuelve_ciudades('Puebla', 'Teziutlan', 'Cholula')
print(next(ciudades))
print(next(ciudades))
print(next(ciudades))
print(next(ciudades))