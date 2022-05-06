#Edgar Moises Hernandez-Gonzalez
#26/10/18-09/11/18
#Pruebas5 Matrices

A = [['Roy',80,75,85,90,95],
	['John',75,80,75,85,100],
	['Dave',80,80,80,90,95]]
print(A)

filas = 2
columnas = 3

B = [0] * filas
for i in range(filas):
    B[i] = [0] * columnas

print(B)

myArray=[[i*j for j in range(3)] for i in range(3)]
print(myArray)