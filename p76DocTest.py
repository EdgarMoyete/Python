import doctest
import math

def triangulo(base, altura):
    """
    calcula area de un triangulo
    >>> triangulo(3, 6)
    9.0

    >>> triangulo(4, 3)
    8.0
    """
    return base * altura / 2

def raiz(listaNumeros):
    """
    retorna lista de sqrt de la listaNumeros
    >>> lista=[]
    >>> for item in [4, 9, 16]:
    ...     lista.append(item)
    >>> raiz(lista)
    [2.0, 3.0, 4.0]

    >>> raiz([64, 81])
    [8.0, 9.0]
    """
    return [math.sqrt(item) for item in listaNumeros]

doctest.testmod()