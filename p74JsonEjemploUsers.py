import json

productos = {
    "producto": ["Refresco", "Galletas", "Jugo", "Agua", "Chocolates", "Leche"],
    "precio": [30, 12, 12, 6, 20, 18],
    "stock": [100, 90, 80, 70, 60, 50]
}

usuarios = [
    {
        "id": 0,
        "nombre": "edgar",
        "correo": "edgar@empresa.com",
        "password": "12345",
        "edad": 26
    },
    {
        "id": 1,
        "nombre": "moises",
        "correo": "moises@empresa.com",
        "password": "qwer",
        "edad": 24
    },
    {
        "id": 2,
        "nombre": "messi",
        "correo": "messi@empresa.com",
        "password": "asd",
        "edad": 35
    },
    {
        "id": 3,
        "nombre": "cristiano",
        "correo": "ronaldo@empresa.com",
        "password": "zxcvbnm",
        "edad": 19
    }
]

print(type(productos))
print("productos", productos)
print(type(usuarios))
print(usuarios)
print(type(usuarios[0]))
print(usuarios[0])

# convertir a JSON:
y = json.dumps(usuarios)
print(type(y))
print(y)