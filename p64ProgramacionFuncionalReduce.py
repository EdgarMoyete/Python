# Edgar Moises Hernandez Gonzalez
# Programacion funcional, lambdas, map, filter y reduce
# 21/06/21
# ejemplo de lambdas y reduce

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sumatoria(lista):
    acumulador = 0
    for item in lista:
        acumulador += item
    return acumulador

print(sumatoria(numeros))
print(reduce(lambda acumulador, elemento: acumulador + elemento, numeros))

lenguajes_programacion=['Python', 'Java', 'C#', 'C++']
print(reduce(lambda acumulador, elemento: acumulador + ' ' + elemento, lenguajes_programacion))

print(reduce(lambda a, b: a*b, range(1,5))) # factorial de 4