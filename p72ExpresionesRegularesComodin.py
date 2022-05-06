import re

lista = ["edgar hernandez gonzalez",
    "edgar gonzalez",
    "moises garcia",
    "alguien garcia",
    "otro garcia",
    "edgar hdez",
    "persona hdez gonzalez"]

print("nombres que comienzan con edgar:")
for item in lista:
    if re.findall("^edgar", item):
        print(item)
    
print("nombres que finalizan con garcia:")
for item in lista:
    if re.findall("garcia$", item):
        print(item)

print("nombres que tiene 'dez':")
for item in lista:
    if re.findall("dez", item):
        print(item)