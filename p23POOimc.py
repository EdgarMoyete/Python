#Edgar Moises Hernandez Gonzalez
#03/01/19
#IMC

class Obesidad:
	def __init__(self, peso, altura):
		self.peso = peso
		self.altura = altura

	def imc(self):
		return self.peso / (self.altura * self.altura)

	def interpretacion(self):
		if self.imc() < 18.5:
			return "Por debajo del peso normal"
		elif self.imc() < 25:
			return "Peso normal"
		elif self.imc() < 30:
			return "Sobrepeso"
		elif self.imc() < 40:
			return "Obesidad"
		else:
			return "Obesidad Severa"

	def informacion(self):
		return "Peso:", self.peso, "Altura:", self.altura, "IMC:", self.imc(), "Interpretacion:", self.interpretacion()

	def __str__(self):
		return "{} {}".format(self.peso, self.altura)

o = Obesidad(86, 1.68)
print(o.informacion())
print(o.__str__())