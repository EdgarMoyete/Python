#Edgar Moises Hernandez-Gonzalez
#24/12/18-03/01/19
#Herencia

class Vehiculo:
	def __init__(self, marca, modelo, enmarcha, acelera, frena):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = enmarcha
		self.acelera = acelera
		self.frena = frena
	
	def arrancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca:", self.marca,
			"\nModelo:", self.modelo,
			"\nEn Marcha:", self.enmarcha,
			"\nAcelera:", self.acelera,
			"\nFrena:", self.frena)

class Moto(Vehiculo):
	def __init__(self, marca, modelo, enmarcha, acelera, frena, hcaballito):
		super().__init__(marca, modelo, enmarcha, acelera, frena)
		self.hcaballito = hcaballito

	def caballito(self):
		self.hcaballito = "Hago caballito"

	def estado(self):
		super().estado()
		print("Caballito:", self.hcaballito)

m = Moto("BMW", "A1", True, False, False, "No")
m.estado()
m.caballito()
m.estado()