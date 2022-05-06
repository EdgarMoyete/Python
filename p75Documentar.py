class Areas:
    """Esto es la documentacion de la clase"""

    def cuadrado(lado):
        """calcula area de un cuadrado"""
        return lado * lado

    def triangulo(base, altura):
        """calcula area de un triangulo"""
        return base * altura / 2

print(Areas.cuadrado.__doc__)
help(Areas)
help(Areas.cuadrado)