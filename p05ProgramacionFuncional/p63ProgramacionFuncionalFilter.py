# Edgar Moises Hernandez Gonzalez
# Programacion funcional
# 19/06/21 - 21/06/21
# ejemplo de lambdas y filter

def is_mayor_edad(edad):
    return edad > 18

def mayores_edad(lista):
    lista_nueva = []
    for item in lista:
        if is_mayor_edad(item):
            lista_nueva.append(item)
    return lista_nueva

lista = [21, 26, 20, 17, 50]

print(mayores_edad(lista))

# filter necesita 2 parametros, el primero debe ser un funcion booleana

print(list(filter(is_mayor_edad, lista)))
print(list(filter(lambda edad: edad > 18, lista)))

def is_par(n):
    return n % 2 == 0

print(list(filter(is_par, range(10))))
print(list(filter(lambda x: x % 2 == 0, range(10))))