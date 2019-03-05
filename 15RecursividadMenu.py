#Edgar Moises Hernandez-Gonzalez
#23/12/18
#Recursividad Menu

def sumatoria(n):
	if n == 0 or n == 1:
		return n
	else:
		return n + sumatoria(n - 1)

def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def sumatoriaCuadrados(n):
	if n == 0 or n == 1:
		return n
	else:
		return n * n + sumatoriaCuadrados(n - 1)

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

n=int(input("Ingrese n: "))
while True:
	print("*****Opciones*****")
	print("Sumatoria:          1")
	print("Factorial:          2")
	print("Sumatoria Cuadrados:3")
	print("Fibonacci:          4")
	print("Salir:              5")
	opcion=int(input("Ingrese opcion: "))
	if opcion == 1:
		print("*Sumatoria*",sumatoria(n))
	elif opcion == 2:
		print("*Factorial*",factorial(n))
	elif opcion == 3:
		print("*Sumatoria Cuadrados*",sumatoriaCuadrados(n))
	elif opcion == 4:
		print("*Fibonacci*",fibonacci(n))
	if opcion > 4:
		break