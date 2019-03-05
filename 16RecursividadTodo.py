#Edgar Moises Hernandez-Gonzalez
#23/12/18-14/01/19
#Recursividad Todo

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

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def cuentaRegresiva(n):
	print(n)
	if n > 0:
		cuentaRegresiva(n - 1)

def potencia(x, y):
	if y == 0:
		return 1
	elif y == 1:
		return x
	else:
		return x*potencia(x, y - 1)

def euclides(m, n):
	if n == 0:
		return m
	else:
		return euclides(n, m % n)

def ackermann(m, n):
	if m == 0:
		return n + 1
	elif n == 0:
		return ackermann(m-1, 1)
	else:
		return ackermann(m - 1, ackermann(m, n - 1))

def particion(n, m):
	if m == 0 or n < 0:
		return 0
	elif n == 0 or m == 1:
		return 1
	elif n == m:
		return 1 + particion(n, m - 1)
	else:
		return particion(n, m - 1) + particion(n - m, m)

def combinacion(n, r):
	if r == 0 or r == n:
		return 1
	elif r == 1:
		return n
	else:
		return combinacion(n - 1, r - 1) + combinacion(n - 1, r)

def catalan(n):
	if n <= 1:
		return 1
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n - i - 1)
	return res

print("Sumatoria:", sumatoria(10))
print("Factorial:", factorial(5))
print("Fibonacci:", fibonacci(10))
cuentaRegresiva(10)
print("Potencia:", potencia(2, 4))
print("Maximo Comun Divisor:", euclides(2353, 1651))
print("Ackermann:", ackermann(2, 3))
print("Particion:", particion(7, 3))
print("Combinacion:", combinacion(10, 4))
print("Catalan:", catalan(5))