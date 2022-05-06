#Edgar Moises Hernandez-Gonzalez
#09/11/18-27/11/18
#Matrices

#crear matriz
matriz = [0] * 6
for i in range(6):
    matriz[i] = [0] * 7

#imprimir matriz
for i in range(len(matriz)):
	for j in range(len(matriz[0])):
		print(matriz[i][j], end=" ")
	print()
print()

#llenar matriz
contar=1;
for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		matriz[i][j]=contar;
		contar+=1;

#imprimir matriz
for i in matriz:
	for j in i:
		print(j, end=" ")
	print()
print()

#imprimir la primer columna de manera inversa
for i in range(len(matriz)-1,-1,-1):
	print(matriz[i][0])