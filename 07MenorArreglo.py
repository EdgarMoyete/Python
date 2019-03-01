#Edgar Moises Hernandez Gonzalez (Moyete)
#17/09/18-25/10/18
#Menor de un arreglo

n=int(input("Ingrese el tamano del arreglo: "))
arreglo=[]
for i in range(n):
	entrada=int(input(f"Ingrese {i}: "))
	arreglo.append(entrada)
menor=arreglo[0]
for i in range(1,len(arreglo)):
	if arreglo[i]<menor:
		menor=arreglo[i]
print("Menor:",menor)