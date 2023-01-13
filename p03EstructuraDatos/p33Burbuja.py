#Edgar Moises Hernandez-Gonzalez
#25/10/18-06/11/18
#Ordenamiento Burbuja

import random

def ordenamientoBurbuja(arreglo):
	aux=0
	for i in range(len(arreglo)-1):
		for j in range(len(arreglo)-1):
			if arreglo[j] > arreglo[j+1]:
				aux=arreglo[j]
				arreglo[j]=arreglo[j+1]
				arreglo[j+1]=aux

#arreglo=[1,0,2,4,5,6,7,3,-1,-2]

arreglo=[]
for i in range(5000): #5000 numeros
	arreglo.append(random.randrange(1000)) #enteros positivos menores a 1000

ordenamientoBurbuja(arreglo)
print(arreglo)