#Edgar Moises Hernandez-Gonzalez
#24/12/18-03/01/19
#Clases y Objetos

class Persona:
	def __init__(self):		
		self.nombre = "Edgar"
		self.edad = 23
	
	def comer(self):
		print("Soy", self.nombre, "y estoy comiendo")		
	
	def cagar(self):
		print("Soy", self.nombre, "y estoy cagando")
	
	def dormir(self):
		print("Soy", self.nombre, "y estoy durmiendo")

	def informacion(self):
		print("Nombre:", self.nombre, "\nEdad: ", self.edad)

p = Persona()
p.comer()
p.cagar()
p.dormir()
p.informacion()

print(p.edad)
p.nombre = "Edgar Moises"
p.informacion()