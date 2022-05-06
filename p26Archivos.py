# Edgar Moises Hernandez-Gonzalez
# 09/01/19 - 21/06/21
# Archivos
"""
archivo = open('texto.txt','w')
archivo.write('Escribiendo en el archivo')
archivo.close()
"""
archivo = open('texto.txt','a')
archivo.write('\nOtra linea nueva')
archivo.close()

archivo = open('texto.txt','r')
print(archivo.read())
archivo.close()

archivo = open('texto.txt','r')
print(archivo.readlines())
archivo.close()

#archivo = open('texto.txt','r+') #lectura y escritura