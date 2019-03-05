#Edgar Moises Hernandez-Gonzalez
#15/11/18
#Pila de la recursion

def recursivo(n):
	print(n)
	if n<10:
		recursivo(n+3)
		print(n,"Dentro")
	print(n,"Fuera")

recursivo(1)