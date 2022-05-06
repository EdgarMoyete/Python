#Edgar Moises Hernandez-Gonzalez
#03/01/19
#Herencia de un circulo a un cilindro

import math

class Circulo:
	def __init__(self, radio):
		self.radio = radio

	def area(self):
		return math.pi * self.radio * self.radio

	def informacion(self):
		return "Radio:", self.radio

class Cilindro(Circulo):
	def __init__(self, radio, altura):
		super().__init__(radio)
		self.altura = altura
		
	def volumen(self):
		return super().area() * self.altura

	def informacion(self):
		return super().informacion(), "Altura:", self.altura

c = Cilindro(5,10)
print(c.informacion())
print("Volumen del Cilindro", c.volumen())