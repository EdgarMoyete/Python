# Edgar Moises Hernandez Gonzalez
# Programacion funcional
# 19/06/21
# ejemplo de lambdas y map

def cuadrado_0(a):
    return a*a

def cuadrado_1(lista):
    lista_nueva = []
    for i in range(len(lista)):
        lista_nueva.append(lista[i] * lista[i])
    return lista_nueva

def cuadrado_1_1(lista):
    lista_nueva = []
    for i in range(len(lista)):
        lista_nueva.append(cuadrado_0(lista[i]))
    return lista_nueva

def cuadrado_2(lista):
    lista_nueva = []
    for item in lista:
        lista_nueva.append(item * item)
    return lista_nueva

def cuadrado_2_1(lista):
    lista_nueva = []
    for item in lista:
        lista_nueva.append(cuadrado_0(item))
    return lista_nueva

lista_cruda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(cuadrado_1(lista_cruda))
print(cuadrado_1_1(lista_cruda))
print(cuadrado_2(lista_cruda))
print(cuadrado_2_1(lista_cruda))

print(list(map(cuadrado_0, lista_cruda)))
print(list(map(lambda a: a*a, lista_cruda)))