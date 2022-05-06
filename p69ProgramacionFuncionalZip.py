# Edgar Moises Hernandez Gonzalez
# Programacion funcional, lambdas, map, filter y reduce
# 21/06/21-19/04/22
# ejemplo de zip

asignaturas = ['Matemáticas', 'Física', 'Química', 'Economía']
notas = [6.0, 3.5, 7.5, 8.0]
juntar = list(zip(asignaturas, notas))
print(juntar)

for asignatura, nota in juntar:
	print("1: La calificacion de la asignatura " + asignatura + " es " + str(nota))
	print("2: La calificacion de la asignatura %s es %s" % (asignatura, nota))

folios = ["123"]
mensajes = ["mensaje1", "mensaje2"]
all = list(zip(folios, mensajes))
print(all)