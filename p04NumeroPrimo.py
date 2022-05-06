#Edgar Moises Hernandez Gonzalez (Moyete)
#17/09/18-18/09/18
#Numero Primo

n=int(input("Ingrese n: "))
contador=0;
for i in range(1,n+1):
	if n%i==0:
		contador+=1
if contador==2:
	print("Si es Primo")
else:
	print("No es Primo")