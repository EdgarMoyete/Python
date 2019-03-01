#Edgar Moises Hernandez-Gonzalez
#05/11/18
#Contar vocales

def contarVocales(cadena):
	cad=cadena.lower()
	vocales=[0, 0, 0, 0, 0]
	for i in cad:
		if i=="a":
			vocales[0]+=1
		elif i=="e":
			vocales[1]+=1
		elif i=="i":
			vocales[2]+=1
		elif i=="o":
			vocales[3]+=1
		elif i=="u":
			vocales[4]+=1
	return vocales

cad=input("Ingrese texto: ")
print(contarVocales(cad))