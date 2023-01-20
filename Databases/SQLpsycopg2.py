from psycopg2 import connect, DatabaseError

from config import PGSQL_USER, PGSQL_PASSWORD, PGSQL_HOST, PGSQL_PORT, PGSQL_DATABASE

def get_conexion():
    try:
        return connect(
            user = PGSQL_USER,
            password = PGSQL_PASSWORD,
            host = PGSQL_HOST,
            port = PGSQL_PORT,
            dbname = PGSQL_DATABASE
        )
    except DatabaseError as error:
        raise error

def consultar():
    conexion = get_conexion()
    with conexion.cursor() as cursor: # al usar with se cierra solo el cursor
        query = """
            SELECT *
            FROM Carreras
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

# insertar("Edecan", 7200)
for item in consultar():
    print(item)