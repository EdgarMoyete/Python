#Edgar Moises Hernandez Gonzalez (Moyete)
#19/09/18-11/05/21
#Pruebas

#listas
lista=[1,2,3,4]
lista.append(5)
print(lista)
lista.insert(1,20)
print(lista)
lista.extend([11,12])
print(lista)

print(lista.index(12))
print(3 in lista)

lista.append("Hola")
print(lista)

lista.remove(20)
print(lista)

lista.pop()
print(lista)

lista2=[33, 44, 55]
print(lista+lista2)

lista3=lista2*5
print(lista3)

print(lista)
print(len(lista))
print(lista.count(5))

lista4=["Edgar","Hernandez","Moyete"]
nombre,paterno,apodo=lista4
print(apodo)
print(paterno)
print(nombre)


#tuplas
tupla=(5,6,7,8,8)
print(tupla)

milista=list(tupla) #convertir una tupla a una lista
print(milista)
print(type(milista))
mitupla=tuple(milista) #convertir una lista a una tupla
print(mitupla)
print(type(mitupla))

print(8 in mitupla)
print(mitupla.count(8))
print(len(mitupla))

tupla2=(20,9,2018)
dia,mes,anio=tupla2
print(anio)
print(mes)
print(dia)