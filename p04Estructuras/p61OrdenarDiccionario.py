edades = {'edgar': 26, 'vale': 20, 'zary': 31, 'luna': 13}
print(edades)

# ordenar por clave
lista_1 = sorted(edades)
print(lista_1)

# ordenar por clave
lista_2 = []
for i in sorted(edades.keys()):
    lista_2.append(i)
print(lista_2)

# ordenar por clave
lista_3 = []
for i in sorted(edades):
    lista_3.append((i, edades[i]))
print(lista_3)

# ordenar por valor
lista_4 = sorted(edades.items(), key = lambda x: (x[1], x[0]))
print(lista_4)

# ordenar por valor
lista_5 = sorted(edades.items(), key = lambda x: x[1])
print(lista_5)

# ordenar por valor en orden descendente
lista_6 = sorted(edades.items(), key = lambda x: x[1], reverse = True)
print(lista_6)

# repetir clave
usuarios = {'edgar0': 0, 'edgar1': 1, 'edgar1': 31}
print(usuarios)