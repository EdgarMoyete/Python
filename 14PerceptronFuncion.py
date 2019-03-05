#Edgar Moises Hernandez-Gonzalez
#30/11/18
#Perceptron

import random

def transpuesta(matriz):
	#crear la matriz filas=columnasMatriz y columnas=filasMatriz
	matrizTranspuesta = [0] * len(matriz[0])
	for i in range(len(matriz[0])):
		matrizTranspuesta[i] = [0] * len(matriz)
	#calcular la transpuesta
	for i in range(len(matriz[0])):
		for j in range(len(matriz)):
			matrizTranspuesta[i][j]=matriz[j][i]
	return matrizTranspuesta

def perceptron(entradas0, objetivos, COEF_APREN, epocas0):
	entradas=transpuesta(entradas0)
	f=len(entradas) #n variables
	c=len(entradas[0]) #n datos
	pesos=[]
	for i in range(f):
		pesos.append(random.random())
	sesgo=random.random()
	for epocas in range(epocas0):
		net=[]
		salidas=[]
		for i in range(c):
			net.append(0)
			for j in range(f):
				net[i]+=(entradas[j][i]*pesos[j]) #producto xi*wi
			net[i]-=sesgo
			if net[i]>=0: #funcion de activacion escalon simetrico
				salidas.append(1)
			else:
				salidas.append(-1)
			delta=objetivos[i]-salidas[i] #regla delta
			for j in range(f):
				pesos[j]+=(COEF_APREN*delta*entradas[j][i]) #actualizacion de los pesos
			sesgo-=(COEF_APREN*delta) #actualizacion de sesgo (bias)
		print("Iteracion",epocas+1)
		print(pesos)
		print(salidas)
	r=[salidas, pesos, sesgo]
	return r

entradas=[
		[0, 0],
		[0, 1],
		[1, 0],
		[1, 1]]
objetivos=[-1, -1, -1, 1]
clasificador=perceptron(entradas, objetivos, 0.7, 10)
print(clasificador) #salidas, pesos y sesgo