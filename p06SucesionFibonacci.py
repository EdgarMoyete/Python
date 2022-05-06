#Edgar Moises Hernandez Gonzalez (Moyete)
#17/09/18-/18/09/18
#Sucesion de Fibonacci

n=int(input("Ingrese n: "))
temporal=0
fibonacci=1
anterior=0
for i in range(1,n+1):
	print(fibonacci)
	temporal=fibonacci
	fibonacci+=anterior
	anterior=temporal