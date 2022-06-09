from psycopg2 import connect, DatabaseError

def get_conexion():
    try:
        return connect(
            user = "postgres",
            password = "12345",
            host = "localhost",
            port = "5432",
            dbname = "empresa"
        )
    except DatabaseError as error:
        raise error

def consultar():
    conexion = get_conexion()
    with conexion.cursor() as cursor: # al usar with se cierra solo el cursor
        query = """
            SELECT *
            FROM appempresa_puestos
        """
        cursor.execute(query)
        rows = cursor.fetchall()
    conexion.close()
    return rows

def insertar(puesto, sueldo):
    conexion = get_conexion()
    with conexion.cursor() as cursor: # al usar with se cierra solo el cursor
        query = """
            INSERT INTO appempresa_puestos (puesto, sueldo)
            VALUES (%s, %s)
        """
        cursor.execute(query, (puesto, sueldo))
        conexion.commit()
    conexion.close()

insertar("Edecan", 7200)
for item in consultar():
    print(item)