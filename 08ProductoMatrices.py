#Edgar Moises Hernandez-Gonzalez
#26/09/18-05/11/18
#Producto de Matrices

def producto(A,B):
	filasA=len(A)
	columnasA=len(A[0])
	filasB=len(B)
	columnasB=len(B[0])

	if columnasA==filasB: #si se pueden multiplicar
		#crear matriz para el resultado
		R = [0] * filasA
		for i in range(filasA):
			R[i] = [0] * columnasB
		#producto de matrices
		for i in range(filasA):
			for j in range(columnasB):
				for k in range(columnasA):
					R[i][j]+=A[i][k]*B[k][j]
	return R

A = [[1,2],
	[4, 5]]
B = [[3,1],
	[-2, 1]]
R=producto(A,B)
print(R)