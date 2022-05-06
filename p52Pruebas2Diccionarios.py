#Edgar Moises Hernandez Gonzalez (Moyete)
#19/09/18-11/05/21
#Pruebas2 (Diccionarios)

diccionario={"Mexico":"CDMX","Jalisco":"Guadalajara","Nuevo Leon":"Monterrey","Puebla":"Puebla de Zaragoza","Veracruz":"Xalapa"}
diccionario["Yucatan"]="Pachuca"
print(diccionario)
diccionario["Yucatan"]="Merida"
print(diccionario)
del diccionario["Veracruz"]
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))
print(type(diccionario))