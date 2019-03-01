#Edgar Moises Hernandez Gonzalez (Moyete)
#17/09/18-18/09/18
#Numero Perfecto

n=int(input("Ingrese n: "))
acumulador=0;
for i in range(1,n):
	if n%i==0:
		acumulador+=i;
if acumulador==n and acumulador>0:
	print("Es Numero Perfecto")
else:
	print("No es Numero Perfecto")