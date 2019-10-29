#Edgar Moises Hernandez-Gonzalez
#03/01/19
#Excepciones

def suma(a, b):
	return a + b
	
def division(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return "ERROR No se puede dividir entre 0"

try:
	a = int(input("Ingrese a: "))
	b = int(input("Ingrese b: "))
except ValueError:
	print("ERROR No seas mamon suma numeros")

try:
	print(suma(a, b))
	print(division(a, b))
except NameError:
	print("ERROR no esta difinida una variable")

print("Programa Ejecutado")