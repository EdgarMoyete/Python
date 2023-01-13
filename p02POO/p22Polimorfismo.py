#Edgar Moises Hernandez-Gonzalez
#03/01/19
#Polimorfismo

class Coche:
	def desplazamiento(self):
		print("Me desplazo en cuatro ruedas")

class Moto:
	def desplazamiento(self):
		print("Me desplazo en dos ruedas")

class Camion:
	def desplazamiento(self):
		print("Me desplazo en seis ruedas")

		
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo = Moto()
desplazamientoVehiculo(miVehiculo)