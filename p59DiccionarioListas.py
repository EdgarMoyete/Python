diccionario = {}
nombre = ['edgar', 'moises', 'pancho', 'andres']
apellido = ['hernandez', 'gonzalez', 'lopez', 'obrador']
edad = [12, 14, 15, 20]
diccionario['nombre'] = nombre
diccionario['apellido'] = apellido
diccionario['edad'] = edad
otro = {}
otro["diccionario"] = diccionario

#print(len(diccionario))
#print(diccionario)
#print(diccionario.keys())
#print(diccionario.values())

print(diccionario['nombre'][0])
print(len(diccionario['nombre']))

print(otro)