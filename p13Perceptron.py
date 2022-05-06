#Edgar Moises Hernandez-Gonzalez
#06/11/18-30/11/18
#Perceptron

import random

entradas0=[
			[0, 0],
			[0, 1],
			[1, 0],
			[1, 1]]
objetivos=[-1, -1, -1, 1]
#Transpuesta de entradas
entradas = [0] * len(entradas0[0])
for i in range(len(entradas0[0])):
    entradas[i] = [0] * len(entradas0)

for i in range(len(entradas0[0])):
	for j in range(len(entradas0)):
		entradas[i][j]=entradas0[j][i]

f=len(entradas) #numero de variables
c=len(entradas[0]) #cantidad de datos

pesos=[]
for i in range(f):
	pesos.append(random.random())
sesgo=random.random()
COEF_APREN=0.7

for epocas in range(5):
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