import sqlite3

conexion = sqlite3.connect("tienda")
cursor = conexion.cursor()

# crear tabla cosas con el id autoincrementable
# cursor.execute('''
#     create table cosas(
#         id integer primary key autoincrement,
#         nombre varchar(20) unique,
#         precio integer
#     )
# ''')

# lista de tuplas para insertar por lotes
# cosas = [
#     ("Agua", 1),
#     ("Galletas", 4),
#     ("Leche", 10),
#     ("Jamon", 80)
# ]

# insertar por lotes
# cursor.executemany("insert into cosas values (null,?,?)", cosas)

# # create
# cursor.execute("insert into cosas values(null, 'cerveza', 16)")

# # update
# cursor.execute("update cosas set precio=2 where id=1")

# # delete
# cursor.execute("delete from cosas where id=4")

# create para evitar SQL Injection
datos = "refresco", 30
cursor.execute("insert into cosas values(null, ?, ?)", (datos))

# read
cursor.execute("select * from cosas")
print(cursor.fetchall())

conexion.commit()
conexion.close()