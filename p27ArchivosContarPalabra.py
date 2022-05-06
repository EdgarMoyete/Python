#Edgar Moises Hernandez-Gonzalez
#09/01/19
#Contar las ocurrencias de una palabra en un archivo

archivo = open('Archivo.txt','r')
cadena=archivo.read()
archivo.close()

busca = input("Ingrese la palabra a buscar: ")
cadena = cadena.lower()
palabras = cadena.split(" ")
cuenta = 0
for i in palabras:
	if i == busca:
		cuenta += 1
print(cuenta)