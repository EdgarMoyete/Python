#Edgar Moises Hernandez-Gonzalez
#23/12/18 - 11/07/21
#Torres de Hanoi

def torresHanoi(n, origen, destino, temporal):
	if n == 1: #mover solo un disco
		print(origen, "-->", destino)
		return
	#mover (n-1) discos de origen a temporal usando destino
	torresHanoi(n-1, origen, temporal, destino)
	#mover el ultimo disco de origen a destino
	print(origen, "-->", destino)
	#mover (n-1) discos de temporal a destino
	torresHanoi(n-1, temporal, destino, origen)

torresHanoi(2, 1, 3, 2)