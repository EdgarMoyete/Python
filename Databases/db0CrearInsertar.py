import sqlite3

conexion = sqlite3.connect("tienda")
cursor = conexion.cursor()
# crear base de datos
# cursor.execute("create table productos(articulo varchar(20), precio integer, seccion varchar(20))")

# insertar un registro
# cursor.execute("insert into productos values('balon', 15, 'deportes')")

# insertar varios registros
# productos = [
#     ("playera", 10, "deportes"),
#     ("jarra", 90, "ceramica"),
#     ("auto", 20, "jugueteria")
# ]
# cursor.executemany("insert into productos values(?,?,?)", productos)

cursor.execute("select * from productos")
productos = cursor.fetchall()
print(type(productos))
print("productos:", productos)

conexion.commit()
conexion.close()