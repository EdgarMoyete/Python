import re

print(re.search("em", "mis iniciales son emhg"))

cad = "vamos a aprender expresiones regulares en python"
busca = "aprender"
objeto = re.search(busca, cad)
if objeto is not None:
    print("si esta")
else:
    print("no esta")

print("indice donde comienza el objeto encontrado:", objeto.start())
print("indice donde termina el objeto encontrado:", objeto.end())
print("los dos indices inicio y fin:", objeto.span())

cadena = "python es un lenguage de programacion interpretado. python tiene varias librerias para ciencia de datos e inteligencia artificial"
print(re.findall("python", cadena))
print(len(re.findall("python", cadena)))