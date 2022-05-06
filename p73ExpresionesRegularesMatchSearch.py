import re

lista = ["qwwe34231dsfg281", "12asdg28op", "2812asdg28op"]

for item in lista:
    print(item)
    if re.match("28", item):
        print("se encontro el patron al comienzo:", item)
    if re.search("28", item):
        print("se encontro el patron en algun lado:", item)
    else:
        print("no se encontro el patron")